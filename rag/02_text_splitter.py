"""
RAG入门：语义切分
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader("test_doc.txt", encoding="utf-8")
documents = loader.load()

# 递归字符切分器：按段落→句子→单词优先级切分
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,      # 每个chunk最大100字符
    chunk_overlap=20,    # 相邻chunk重叠20字符（保持上下文连贯）
    separators=["\n\n", "\n", "。", " ", ""],  # 切分优先级
)

chunks = splitter.split_documents(documents)

print(f"切分后共 {len(chunks)} 个chunk")
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk.page_content)
