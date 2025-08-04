from django.shortcuts import render
from rest_framework import generics
from .models import BuffetItem, MenuItem, OrderInfo
from .serializers import BuffetItemSerializer, MenuItemSerializer, OrderSerializer
from django.http import JsonResponse

import os
import json

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
SYSTEM = "You are City King Buffet's friendly AI. Always begin your reply with 'My friend!' then answer the question."
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(SYSTEM),
    HumanMessagePromptTemplate.from_template(
        "Here's some background:\n\n"
        "{context}\n\n"
        "Now answer:\n\n"
        "{question}"
    ),
])

def chat(request):
    q = request.GET.get("q","")
    if not q:
        return JsonResponse({"error":"No question provided"}, status=400)

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
    answer = qa.run(q)
    return JsonResponse({"answer": answer})


# GET all menu items
class BuffetItemList(generics.ListAPIView):
    queryset = BuffetItem.objects.all()
    serializer_class = BuffetItemSerializer

class MenuItemList(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# POST an order
class OrderCreate(generics.CreateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderSerializer


