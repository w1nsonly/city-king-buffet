# utils/is_restaurant_question

from langchain.chat_models      import ChatOpenAI

# Add the classification LLM (separate from your main QA chain)
classification_llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

def is_restaurant_question(question: str) -> bool:
    """Check if a question is related to City King Buffet or is a greeting."""
    
    # Allow common greetings and casual conversation starters
    greetings = {
        'hey', 'hello', 'hi', 'howdy', 'greetings', 'good morning', 
        'good afternoon', 'good evening', 'what\'s up', 'whats up',
        'how are you', 'how\'s it going', 'hows it going'
    }
    
    question_lower = question.lower().strip()
    
    # Check if it's just a greeting
    if any(greeting in question_lower for greeting in greetings):
        return True
    
    classification_prompt = f"""Is this question related to City King Buffet restaurant specifically, or about restaurants/food/dining in general that could be answered about City King Buffet?
        If the answer is answerable using the faq.txt, then please allow the response to be yes.
        Examples of YES:
        - "What are your hours?"
        - "Do you have seafood?"
        - "How much does it cost?"
        - "Where are you located?"
        - "What kind of food do you serve?"
        - "Do you take reservations?"
        - "Who is the owner?"
        - "Who is Denny Dong?"
        - "What happened in 2014?"
        - "Do you have beer?"
        - "How much is it right now?"

        Examples of NO:
        - "Do you guys have senior discount?"
        - "What's the weather?"
        - "How do I fix my car?"
        - "Tell me about other restaurants"
        - "What's 2+2?"

        Answer only "YES" or "NO".
        Question: {question}"""
    
    try:
        response = classification_llm.invoke(classification_prompt)
        return "YES" in response.content.upper()
    except Exception:
        # If classification fails, err on the side of allowing the question
        return True