# utils/pricing_and_hours.py

from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo
import re

# Local timezone 
LOCAL_TZ = ZoneInfo("America/New_York")

# Open/close by weekday (0=Mon … 6=Sun)
HOURS = {
    0: (time(11, 0),  time(21, 0)),   # Mon
    1: (time(11, 0),  time(21, 0)),   # Tue
    2: (time(11, 0),  time(21, 0)),   # Wed
    3: (time(11, 0),  time(21, 0)),   # Thu
    4: (time(11, 0),  time(21,30)),   # Fri
    5: (time(11, 0),  time(21,30)),   # Sat
    6: (time(11,30),  time(21,30)),   # Sun
}

# Prices
PRICES = {
    "adult_lunch":            11.99,
    "adult_weekday_dinner":   14.99,
    "adult_weekend_dinner":   15.99,
    "kid_3_5_lunch":           6.99,
    "kid_6_10_lunch":          7.99,
    "kid_3_5_dinner":          7.99,
    "kid_6_10_dinner":         9.99,
}

# Lunch window + weekend days
LUNCH_START = time(11, 0)
LUNCH_END   = time(16, 0)  # exclusive
WEEKEND_DAYS = {4, 5, 6}   # Fri, Sat, Sun

# Detect "price right now" (or just "price")
PRICE_NOW_RE = re.compile(
    r"(price|cost|how much).*(now|right now|today|currently)|^\s*price\s*$",
    re.IGNORECASE,
)

# ------ HELPER FUNCTIONS ------
def now_local() -> datetime:
    """Return timezone-aware 'now' in LOCAL_TZ."""
    return datetime.now(LOCAL_TZ)

def today_hours(now: datetime):
    """Return (open_time, close_time) for the given datetime's weekday."""
    return HOURS[now.weekday()]

def is_open(now: datetime) -> bool:
    """Whether the restaurant is open at the given local datetime."""
    open_time, close_time = today_hours(now)
    return open_time <= now.time() <= close_time

def next_open_datetime(now: datetime) -> datetime:
    """Find the next opening datetime from 'now'."""
    for i in range(0, 8):
        day = now + timedelta(days=i)
        open_time, close_time = HOURS[day.weekday()]
        # Today: before open -> today at open
        if i == 0 and now.time() < open_time:
            return day.replace(hour=open_time.hour, minute=open_time.minute, second=0, microsecond=0)
        # Today: already closed -> check tomorrow
        if i == 0 and now.time() >= close_time:
            continue
        # Future day: return that day's open
        if i > 0:
            return day.replace(hour=open_time.hour, minute=open_time.minute, second=0, microsecond=0)
    return now  # fallback

def current_prices(now: datetime):
    """
    Return tuple: (meal, prices)
      meal: 'lunch' or 'dinner'
      prices: { 'adult': float, 'kids': {'3_5': float, '6_10': float} }
    """
    # Sunday: always dinner pricing
    if now.weekday() == 6:  # Sunday
        meal = "dinner"
        adult = PRICES["adult_weekend_dinner"]
        kids = {
            "3_5": PRICES["kid_3_5_dinner"],
            "6_10": PRICES["kid_6_10_dinner"],
        }
        return meal, {"adult": adult, "kids": kids}
    
    if LUNCH_START <= now.time() < LUNCH_END:
        meal = "lunch"
        adult = PRICES["adult_lunch"]
        kids = {"3_5": PRICES["kid_3_5_lunch"], "6_10": PRICES["kid_6_10_lunch"]}
    else:
        meal = "dinner"
        adult = (PRICES["adult_weekend_dinner"]if now.weekday() in WEEKEND_DAYS
            else PRICES["adult_weekday_dinner"]
        )
        kids = {"3_5": PRICES["kid_3_5_dinner"], "6_10": PRICES["kid_6_10_dinner"]}
    return meal, {"adult": adult, "kids": kids}

def is_price_now_question(q: str) -> bool:
    """Heuristic: is the user asking for the price 'right now' (or just 'price')?"""
    return bool(PRICE_NOW_RE.search(q))

def _when_open(now: datetime, nxt: datetime) -> str:
    """Return 'today at 11:00 AM', 'tomorrow at 11:00 AM', or 'Sat at 11:00 AM'."""
    t = nxt.strftime("%I:%M %p").lstrip("0")
    if nxt.date() == now.date():
        return f"today at {t}"
    if nxt.date() == (now + timedelta(days=1)).date():
        return f"tomorrow at {t}"

def get_price_now_answer() -> str:
    """
    If open: say the current meal price (adult + kids).
    If closed: say when we open next + tomorrow's meal price (adult + kids).
    """
    now = now_local()

    # Closed branch
    if not is_open(now):
        nxt = next_open_datetime(now)
        meal, prices = current_prices(nxt)
        adult_price     = prices["adult"]
        kids_3_5_price  = prices["kids"]["3_5"]
        kids_6_10_price = prices["kids"]["6_10"]

        return (
            f"My friend! We're currently closed. We open {_when_open(now, nxt)}. "
            f"For {meal}, tomorrow's price will be ${adult_price:.2f}. "
            f"Kids ages (6-10): ${kids_6_10_price:.2f}, Kids ages (3-5): ${kids_3_5_price:.2f}."
        )

    # Open branch
    meal, prices = current_prices(now)
    adult_price     = prices["adult"]
    kids_3_5_price  = prices["kids"]["3_5"]
    kids_6_10_price = prices["kids"]["6_10"]

    return (
        f"My friend! Right now it's ${adult_price:.2f} for {meal}. "
        f"Kids (6-10): ${kids_6_10_price:.2f}, Kids (3-5): ${kids_3_5_price:.2f}."
    )


# --- Detect "price on <weekday>" (and optional lunch/dinner) ---
DAY_PRICE_RE = re.compile(
    r"(?:price|cost|how much).*?\bon\s*"
    r"(mon(day)?|tue(s|sday)?|wed(nesday)?|thu(r|rs|rsday)?|fri(day)?|sat(urday)?|sun(day)?)\b"
    r"|"
    r"\b(mon(day)?|tue(s|sday)?|wed(nesday)?|thu(r|rs|rsday)?|fri(day)?|sat(urday)?|sun(day)?)\b.*?(?:price|cost|how much)",
    re.IGNORECASE,
)

DAY_ALIASES = {
    "mon": 0, "monday": 0,
    "tue": 1, "tues": 1, "tuesday": 1,
    "wed": 2, "weds": 2, "wednesday": 2,
    "thu": 3, "thur": 3, "thurs": 3, "thursday": 3,
    "fri": 4, "friday": 4,
    "sat": 5, "saturday": 5,
    "sun": 6, "sunday": 6,
}

MEAL_RE = re.compile(r"\b(lunch|dinner)\b", re.IGNORECASE)

def is_price_specific_day_question(q: str) -> bool:
    return bool(DAY_PRICE_RE.search(q))

def _extract_weekday(q: str) -> int | None:
    m = DAY_PRICE_RE.search(q)
    if not m:
        return None
    # pick the first non-None matched day group
    for i in range(1, m.lastindex + 1 if m.lastindex else 1):
        g = m.group(i)
        if g:
            name = g.lower()
            if name.startswith("tues"): name = "tues"
            if name.startswith("weds"): name = "weds"
            if name.startswith("thurs") or name.startswith("thur"): name = "thurs"
            return DAY_ALIASES.get(name)
    return None

def _extract_meal(q: str) -> str | None:
    m = MEAL_RE.search(q)
    return m.group(1).lower() if m else None

def _human_weekday(w: int) -> str:
    return ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][w]

def _dt_for_weekday(now: datetime, w: int) -> datetime:
    """Next occurrence of that weekday (including today if later today)."""
    days_ahead = (w - now.weekday()) % 7
    target = now + timedelta(days=days_ahead)
    return target.replace(hour=12, minute=0, second=0, microsecond=0)

def get_price_for_weekday_answer(q: str) -> str:
    w = _extract_weekday(q)
    if w is None:
        return "My friend! Please ask like: 'price on Tuesday'."

    meal_hint = _extract_meal(q)  # 'lunch' or 'dinner' or None
    now = now_local()
    target = _dt_for_weekday(now, w)

    # Sunday: dinner pricing all day (your rule)
    if w == 6:
        meal, prices = current_prices(target.replace(hour=18, minute=0))  # ensure dinner
        a = prices["adult"]; k35 = prices["kids"]["3_5"]; k610 = prices["kids"]["6_10"]
        return (f"My friend! On Sunday, dinner pricing applies all day: "
                f"adults ${a:.2f}, kids (6-10) ${k610:.2f}, kids (3-5) ${k35:.2f}.")

    day_str = _human_weekday(w)

    # If user asked for a specific meal
    if meal_hint == "lunch":
        meal, prices = current_prices(target.replace(hour=LUNCH_START.hour, minute=LUNCH_START.minute))
        a = prices["adult"]; k35 = prices["kids"]["3_5"]; k610 = prices["kids"]["6_10"]
        return (f"My friend! On {day_str} lunch: adults ${a:.2f}, "
                f"kids (6-10) ${k610:.2f}, kids (3-5) ${k35:.2f}.")
    if meal_hint == "dinner":
        meal, prices = current_prices(target.replace(hour=LUNCH_END.hour, minute=LUNCH_END.minute))
        a = prices["adult"]; k35 = prices["kids"]["3_5"]; k610 = prices["kids"]["6_10"]
        return (f"My friend! On {day_str} dinner: adults ${a:.2f}, "
                f"kids (6-10) ${k610:.2f}, kids (3-5) ${k35:.2f}.")

    # No meal specified → show both (except Sunday handled above)
    mealL, pricesL = current_prices(target.replace(hour=LUNCH_START.hour, minute=LUNCH_START.minute))
    mealD, pricesD = current_prices(target.replace(hour=LUNCH_END.hour, minute=LUNCH_END.minute))
    aL = pricesL["adult"]; k35L = pricesL["kids"]["3_5"]; k610L = pricesL["kids"]["6_10"]
    aD = pricesD["adult"]; k35D = pricesD["kids"]["3_5"]; k610D = pricesD["kids"]["6_10"]

    return (f"My friend! On {day_str}: "
            f"lunch ${aL:.2f} (kids 6-10 ${k610L:.2f}, 3-5 ${k35L:.2f}); "
            f"dinner ${aD:.2f} (kids 6-10 ${k610D:.2f}, 3-5 ${k35D:.2f}).")


# to detect "hours today?" 
HOURS_TODAY_RE = re.compile(
    r"(hours?|open|close|closing).*(today|tonight|now)|^\s*(what are your hours|hours\?)\s*$",
    re.IGNORECASE,
)

def is_hours_today_question(q: str) -> bool:
    return bool(HOURS_TODAY_RE.search(q))


def _format_time(t: time) -> str:
    # 12-hour like "11:00 AM"
    return datetime(2000, 1, 1, t.hour, t.minute).strftime("%I:%M %p").lstrip("0")


def get_hours_today_answer() -> str:
    """
    If before opening: say today's open & close.
    If open now: say today's range and remind close time.
    If already closed: say we closed for today and when we open next.
    """
    now = now_local()
    open_time, close_time = today_hours(now)
    open_str = _format_time(open_time)
    close_str = _format_time(close_time)

    if now.time() < open_time:
        return f"My friend! Today we're open {open_str}-{close_str}."
    if open_time <= now.time() <= close_time:
        return f"My friend! Today we're open {open_str}-{close_str}. We close at {close_str}."
    # after close
    nxt = next_open_datetime(now)
    when_txt = _when_open(now, nxt)
    return f"My friend! We're closed for today. We reopen {when_txt}."