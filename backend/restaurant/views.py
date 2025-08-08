# restaurant/views.py
from django.shortcuts import render
from rest_framework import generics
from .models import BuffetItem, MenuItem
from .serializers import BuffetItemSerializer, MenuItemSerializer
from django.http import JsonResponse

import os
import json
import openai

from django.views.decorators.http import require_GET
from langchain.schema           import Document
from langchain.text_splitter    import CharacterTextSplitter
from langchain_openai           import OpenAIEmbeddings
from langchain.chat_models      import ChatOpenAI
from langchain.chains           import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


# OPENAI_API_KEY is in the environment
os.environ.setdefault("OPENAI_API_KEY", "")

# Create your views here.
SYSTEM = "You are City King Buffet's friendly AI. " \
        "Always begin your reply with 'My friend!' then answer the question. " \
        "If the user types just 'price' default to list buffet prices." \
        "Also, for your responses, dont provide any unncessary suggestions. Just give your answers from the faqs.txt"
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(SYSTEM),
    HumanMessagePromptTemplate.from_template(
        "Here's some background:\n\n"
        "{context}\n\n"
        "Now answer:\n\n"
        "{question}"
    ),
])

# Initialize once at import time (so you don’t rebuild every request)
store = Chroma(
    persist_directory="chroma_db",
    embedding_function=OpenAIEmbeddings()
)
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4o-mini"),
    chain_type="stuff",
    retriever=store.as_retriever(k=4),
    chain_type_kwargs={"prompt": prompt},
)

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

        Examples of NO:
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

def chat(request):
    q = request.GET.get("q", "").strip()
    if not q:
        return JsonResponse({"error": "No question provided"}, status=400)

    # 1) Classification step
    if not is_restaurant_question(q):
        return JsonResponse({
            "answer": (
                "Sorry, I can't answer that."
            )
        })

    # 2) Otherwise, run your normal QA pipeline
    answer = qa.run(q)
    return JsonResponse({"answer": answer})


# GET all menu items
class BuffetItemList(generics.ListAPIView):
    queryset = BuffetItem.objects.all()
    serializer_class = BuffetItemSerializer

class MenuItemList(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

