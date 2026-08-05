"""
RAG入门：Embedding + Chroma向量数据库
"""

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# 1. 加载 + 切分
loader = TextLoader("test_doc.txt", encoding="utf-8")
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
chunks = splitter.split_documents(documents)

# 2. Embedding（调用API将文本转为向量）
embeddings = OpenAIEmbeddings(
    base_url="https://api.deepseek.com/v1",
    api_key="your-api-key",
    model="deepseek-embedding",  # 或 text-embedding-3-small
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
