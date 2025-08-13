# restaurant/views.py

from django.shortcuts import render
from rest_framework import generics
from .models import BuffetCategory, BuffetItem, KitchenCategory, KitchenItem
from .serializers import BuffetCategorySerializer, BuffetItemSerializer, KitchenCategorySerializer, KitchenItemSerializer
from django.http import JsonResponse
from django.db import connection

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
from utils.is_restaurant_question import is_restaurant_question
from utils.pricing_and_hours import (
    is_price_now_question, get_price_now_answer,
    is_hours_today_question, get_hours_today_answer,
    is_price_specific_day_question, get_price_for_weekday_answer,
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

def chat(request):
    q = request.GET.get("q", "").strip()
    if not q:
        return JsonResponse({"error": "No question provided"}, status=400)
    
    # Short-circuits
    if is_price_now_question(q):
        return JsonResponse({"answer": get_price_now_answer()})
    if is_price_specific_day_question(q):
        return JsonResponse({"answer": get_price_for_weekday_answer(q)})
    if is_hours_today_question(q):
        return JsonResponse({"answer": get_hours_today_answer()})
    
    # Classification step
    if not is_restaurant_question(q):
        return JsonResponse({"answer": ("Sorry, I can't answer that.")
        })

    # 2) Otherwise, run normal QA pipeline
    answer = qa.run(q)
    return JsonResponse({"answer": answer})



# GET all category
class BuffetCategoryList(generics.ListAPIView):
    queryset = BuffetCategory.objects.all()
    serializer_class = BuffetCategorySerializer

class KitchenCategoryList(generics.ListAPIView):
    queryset = KitchenCategory.objects.all()
    serializer_class = KitchenCategorySerializer


# GET all menu items
class BuffetItemList(generics.ListAPIView):
    queryset = BuffetItem.objects.all()
    serializer_class = BuffetItemSerializer

class KitchenItemList(generics.ListAPIView):
    queryset = KitchenItem.objects.select_related("category").all()
    serializer_class = KitchenItemSerializer





# To keep backend alive
def keepalive(request):
    return JsonResponse({"ok": True})

