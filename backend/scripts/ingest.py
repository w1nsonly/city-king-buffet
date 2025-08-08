# scripts/ingest.py

import os
from langchain_community.document_loaders import JSONLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# 1) Make sure your key is set
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# 2) Load buffet.json
buffet_loader = JSONLoader(
    file_path="data/buffet.json",
    jq_schema=(
        '.[] | {'
        ' text: (.category + " " + .name + " — $" + (.price|tostring)),'
        ' metadata: {category: .category, name: .name, price: .price}'
        '}'
    ),
    text_content=False
)
buffet_docs = buffet_loader.load()

# 3) Load menu.json
menu_loader = JSONLoader(
    file_path="data/menu.json",
    jq_schema=(
        '.[] | {'
        ' text: (.category + " " + .name + " — $" + (.price|tostring)),'
        ' metadata: {category: .category, name: .name, price: .price}'
        '}'
    ),
    text_content=False
)
menu_docs = menu_loader.load()

# 4) Load faqs.txt
faq_loader = TextLoader("data/faqs.txt")
faq_docs = faq_loader.load()

# 5) Combining docs
combined_docs = buffet_docs + menu_docs + faq_docs

# 6) Chunk into ~500-char pieces
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks   = splitter.split_documents(combined_docs)

# 7) Embed & persist to Chroma
store = Chroma.from_documents(
    documents=chunks,
    embedding=OpenAIEmbeddings(),
    persist_directory="chroma_db"
)
store.persist()

print("Ingestion complete. Created `chroma_db/` folder.")
