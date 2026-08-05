"""
RAG入门：完整流程（检索 + LLM生成）
"""

import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# 1. 加载文档
loader = TextLoader("test_doc.txt", encoding="utf-8")
documents = loader.load()

# 2. 切分
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
chunks = splitter.split_documents(documents)

# 3. Embedding + 向量库
embeddings = OpenAIEmbeddings(
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    model="deepseek-embedding",
)
vectorstore = Chroma.from_documents(chunks, embeddings)

# 4. 检索
query = "FastAPI有什么优势？"
retrieved_docs = vectorstore.similarity_search(query, k=2)
context = "\n\n".join([doc.page_content for doc in retrieved_docs])

# 5. 构造Prompt（检索结果 + 用户问题）
prompt = f"""基于以下文档片段回答问题：

{context}

问题：{query}
请用中文简洁回答。"""

# 6. LLM生成
llm = ChatOpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    model="deepseek-chat",
)

response = llm.invoke(prompt)
print(response.content)