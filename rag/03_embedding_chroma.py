"""
RAG入门：Embedding + Chroma向量数据库
"""

import os
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
load_dotenv()

# 1. 加载 + 切分
loader = TextLoader("test_doc.txt", encoding="utf-8")
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
chunks = splitter.split_documents(documents)

API_KEY = os.getenv("QW_API_KEY")
# 2. Embedding（调用API将文本转为向量）
embeddings = DashScopeEmbeddings(
    dashscope_api_key=API_KEY,
    model="text-embedding-v3",
)

# 3. 存入Chroma向量库
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db",  # 本地持久化目录
)

print("向量库创建完成")

# 4. 检索相似片段
query = "FastAPI的性能如何？"
results = vectorstore.similarity_search(query, k=2)

print(f"\n查询: {query}")
print(f"检索到 {len(results)} 个相关片段:\n")
for i, doc in enumerate(results):
    print(f"--- 片段 {i+1} ---")
    print(doc.page_content)
