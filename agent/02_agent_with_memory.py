"""
Agent进阶：带记忆的对话
- 使用Checkpointer保存状态
- 支持多轮对话
"""

from langgraph.checkpoint.memory import MemorySaver

# 在编译时添加记忆
memory = MemorySaver()
graph = builder.compile(checkpointer=memory)

# 运行时需要传入thread_id区分对话
config = {"configurable": {"thread_id": "user_123"}}
result = graph.invoke({"messages": ["你好"]}, config=config)

# 再次调用时，会自动加载该thread_id的历史状态
result2 = graph.invoke({"messages": ["刚才我问了什么？"]}, config=config)