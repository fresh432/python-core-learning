"""
Agent进阶：LangGraph + 真实LLM + 工具调用完整链路
- DeepSeek API 真实调用
- 3个工具：搜索/计算/获取时间
- 自动决策：LLM自己决定要不要调用工具
"""

import os
from typing import TypedDict, Annotated
import operator

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode


# ========== 1. 定义工具 ==========

@tool
def search_docs(query: str) -> str:
    """搜索技术文档知识库，回答技术问题"""
    # 学习阶段用mock
    docs = {
        "fastapi": "FastAPI是一个现代Python Web框架，基于Starlette和Pydantic，性能接近Go和Node.js",
        "redis": "Redis是内存数据库，支持缓存、消息队列、分布式锁等场景",
    }
    for key, value in docs.items():
        if key in query.lower():
            return f"[知识库] {value}"
    return "[知识库] 未找到相关内容"


@tool
def calculate(expression: str) -> str:
    """数学计算器，支持加减乘除"""
    try:
        # 安全计算：只允许数字和运算符
        allowed = set("0123456789+-*/.() ")
        if not all(c in allowed for c in expression):
            return "错误：包含非法字符"
        result = eval(expression)
        return f"计算结果：{result}"
    except Exception as e:
        return f"计算失败：{e}"


@tool
def get_time() -> str:
    """获取当前时间"""
    from datetime import datetime
    return datetime.now().strftime("当前时间：%Y-%m-%d %H:%M:%S")


# 工具列表
tools = [search_docs, calculate, get_time]

# ToolNode：自动执行工具调用
tool_node = ToolNode(tools)


# ========== 2. 定义状态 ==========

class AgentState(TypedDict):
    # messages自动累加，保存完整对话历史
    messages: Annotated[list, operator.add]


# ========== 3. LLM配置（绑定工具） ==========

llm = ChatOpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    model="deepseek-chat",
    temperature=0.3,  # Agent用低温度，确定性高
)

# 关键：bind_tools让LLM知道有哪些工具可用
llm_with_tools = llm.bind_tools(tools)


# ========== 4. 节点定义 ==========

def agent_node(state: AgentState):
    """
    Agent思考节点
    - LLM看到用户问题和历史，决定：直接回答 / 调用工具
    - 如果调用工具，会在message中生成tool_calls字段
    """
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


# ========== 5. 条件路由 ==========

def should_continue(state: AgentState):
    """
    判断是否需要继续调用工具
    - 检查最后一条message是否有tool_calls
    """
    last_message = state["messages"][-1]

    # LLM决定调用工具时，会生成tool_calls字段
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "continue"  # 去tools节点执行工具
    return "end"  # 直接结束，返回答案


# ========== 6. 构建状态图 ==========

builder = StateGraph(AgentState)

# 添加节点
builder.add_node("agent", agent_node)   # LLM思考
builder.add_node("tools", tool_node)    # 工具执行

# 入口
builder.set_entry_point("agent")

# 条件边：agent → tools 或 agent → END
builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",  # 有tool_calls，执行工具
        "end": END,            # 无tool_calls，结束
    }
)

# 工具执行完后，回到agent继续思考
builder.add_edge("tools", "agent")

# 编译
graph = builder.compile()


# ========== 7. 测试 ==========

if __name__ == "__main__":

    print("=" * 50)
    print("测试1：直接问答（不需要工具）")
    print("=" * 50)
    result = graph.invoke({
        "messages": [{"role": "user", "content": "你好，请介绍一下自己"}]
    })
    for msg in result["messages"]:
        msg_type = getattr(msg, "type", None) or msg.get("type", "unknown")
        msg_content = getattr(msg, "content", None) or msg.get("content", "")
        print(f"{msg_type}: {str(msg_content)[:100]}...")

    print("\n" + "=" * 50)
    print("测试2：需要计算工具")
    print("=" * 50)
    result = graph.invoke({
        "messages": [{"role": "user", "content": "123乘以456等于多少？"}]
    })
    for msg in result["messages"]:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            print(f"🛠️ tool_calls: {msg.tool_calls}")
        else:
            msg_type = getattr(msg, "type", None) or msg.get("type", "unknown")
            msg_content = getattr(msg, "content", None) or msg.get("content", "")
            print(f"{msg_type}: {str(msg_content)[:100]}...")

    print("\n" + "=" * 50)
    print("测试3：需要搜索工具")
    print("=" * 50)
    result = graph.invoke({
        "messages": [{"role": "user", "content": "FastAPI有什么优势？"}]
    })
    for msg in result["messages"]:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            print(f"🛠️ tool_calls: {msg.tool_calls}")
        else:
            msg_type = getattr(msg, "type", None) or msg.get("type", "unknown")
            msg_content = getattr(msg, "content", None) or msg.get("content", "")
            print(f"{msg_type}: {str(msg_content)[:100]}...")

    print("\n" + "=" * 50)
    print("测试4：需要多个工具")
    print("=" * 50)
    result = graph.invoke({
        "messages": [{"role": "user", "content": "现在几点了？顺便算一下100+200"}]
    })
    for msg in result["messages"]:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            print(f"🛠️ tool_calls: {msg.tool_calls}")
        else:
            msg_type = getattr(msg, "type", None) or msg.get("type", "unknown")
            msg_content = getattr(msg, "content", None) or msg.get("content", "")
            print(f"{msg_type}: {str(msg_content)[:100]}...")