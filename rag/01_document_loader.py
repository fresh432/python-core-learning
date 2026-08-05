"""
RAG入门：文档加载
"""

from langchain_community.document_loaders import TextLoader

# 加载本地文本文件
loader = TextLoader("test_doc.txt", encoding="utf-8")
documents = loader.load()

print(f"加载了 {len(documents)} 个文档")
print(f"第一个文档内容长度: {len(documents[0].page_content)}")
print(f"元数据: {documents[0].metadata}")