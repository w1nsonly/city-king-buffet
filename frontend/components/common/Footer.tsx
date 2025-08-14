// components/common/Footer.tsx

export default function Footer() {
    
    return (
        <footer className="bg-[#7D1918] text-[#F9EBCD] py-20 px-4 sm:px-10">
            <div className="wrapper w-full max-w-[70rem] mx-auto flex flex-col items-center text-center gap-10
                            sm:flex-row sm:items-start sm:text-left sm:justify-center sm:gap-[3.75rem]">
                <div className="footer-address flex-none">
                    <h3 className="text-base font-bold uppercase tracking-[0.15em] mb-3">Address</h3>
                        <p className="text-sm text-white leading-[1.6] my-1.5">705 Maysville Road</p>
                        <p className="text-sm text-white leading-[1.6] my-1.5">Mt. Sterling, KY 40353</p>
                </div>

                <div className="footer-hours flex-none">
                    <h3 className="text-base font-bold uppercase tracking-[0.15em] mb-3">Opening Hours</h3>
                        <p className="text-sm text-white leading-[1.6] my-1.5">Mon - Thu: 11: AM - 9 PM</p>
                        <p className="text-sm text-white leading-[1.6] my-1.5">Fri - Sat: 11: AM - 9:30 PM</p>
                        <p className="text-sm text-white leading-[1.6] my-1.5">Sun: 11:30 AM - 9 PM</p>
                </div>

                <div className="footer-contact flex-none">
                    <h3 className="text-base font-bold uppercase tracking-[0.15em] mb-3">Contact</h3>
                    <p className="text-sm text-white leading-[1.6] my-1.5">
                        <a href="tel:8594988088" className="underline">859-498-8088</a>
                    </p>
                </div>
            </div>
        </footer>
    );
}
