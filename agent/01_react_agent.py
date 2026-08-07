"""
Agent入门：ReAct模式（Reasoning + Acting）
- LLM思考：我需要做什么？
- 调用工具：执行搜索/计算等
- 观察结果：工具返回了什么？
- 继续思考：基于结果继续...
"""

from typing import TypedDict, Annotated
import operator
from langgraph.graph import StateGraph, END


# ========== 定义状态 ==========

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]  # 消息历史，自动累加
    next_step: str  # 下一步动作：think / search / calculate / answer


# ========== 定义节点 ==========

def llm_think(state: AgentState):
    """LLM思考节点：决定下一步做什么"""
    last_msg = state["messages"][-1] if state["messages"] else ""

    # 简单规则模拟（实际应调用LLM）
    if "天气" in last_msg:
        return {"next_step": "search", "messages": ["[思考] 用户问天气，需要搜索"]}
    elif "计算" in last_msg or "+" in last_msg:
        return {"next_step": "calculate", "messages": ["[思考] 用户要计算，需要计算器"]}
    else:
        return {"next_step": "answer", "messages": ["[思考] 直接回答即可"]}


def search_tool(state: AgentState):
    """搜索工具节点（模拟）"""
    return {"messages": ["[工具结果] 北京今天晴，25-32℃"]}


def calculate_tool(state: AgentState):
    """计算工具节点（模拟）"""
    return {"messages": ["[工具结果] 计算结果 = 42"]}


def llm_answer(state: AgentState):
    """LLM生成最终回答"""
    return {"messages": ["[回答] 基于以上信息，答案是..."]}


# ========== 构建状态图 ==========

builder = StateGraph(AgentState)

# 添加节点
builder.add_node("think", llm_think)
builder.add_node("search", search_tool)
builder.add_node("calculate", calculate_tool)
builder.add_node("answer", llm_answer)

# 添加边
builder.set_entry_point("think")


# 条件边：根据next_step决定路由
def route(state: AgentState):
    return state["next_step"]


builder.add_conditional_edges(
    "think",
    route,
    {
        "search": "search",
        "calculate": "calculate",
        "answer": "answer",
    }
)

# 工具执行完后回到思考节点
builder.add_edge("search", "think")
builder.add_edge("calculate", "think")

# 回答结束
builder.add_edge("answer", END)

# 编译
graph = builder.compile()

# ========== 运行 ==========

if __name__ == "__main__":
    result = graph.invoke({"messages": ["北京今天天气怎么样？"]})
    for msg in result["messages"]:
        print(msg)