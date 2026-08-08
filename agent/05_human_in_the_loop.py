"""
Agent进阶：Human-in-the-loop（人工确认）
- 执行敏感操作前暂停，等待人类确认
- 适用场景：删除数据、发送邮件、执行转账等
"""

import os
from typing import TypedDict, Annotated
import operator

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode


# ========== 1. 定义工具（含敏感操作） ==========

@tool
def query_data(query: str) -> str:
    """查询数据（安全操作，无需确认）"""
    return f"[查询结果] 关于 '{query}' 的数据：xxx"


@tool
def delete_data(table: str, id: int) -> str:
    """
    删除数据（敏感操作，需要人工确认）
    ⚠️ 执行前会暂停等待确认
    """
    return f"[执行结果] 已删除 {table} 表中 id={id} 的数据"


tools = [query_data, delete_data]
tool_node = ToolNode(tools)


# ========== 2. 定义状态 ==========

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]


# ========== 3. LLM配置 ==========

llm = ChatOpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    model="deepseek-chat",
    temperature=0.3,
)
llm_with_tools = llm.bind_tools(tools)


# ========== 4. 节点定义 ==========

def agent_node(state: AgentState):
    """Agent思考节点"""
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


def should_continue(state: AgentState):
    """判断是否继续调用工具"""
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "continue"
    return "end"


# ========== 5. 构建图（关键：interrupt_before） ==========

builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
builder.add_node("tools", tool_node)

builder.set_entry_point("agent")

builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "end": END,
    }
)

builder.add_edge("tools", "agent")

# 关键：在 tools 节点前设置中断
# 当LLM决定调用工具时，会在进入tools节点前暂停，等待人类确认
graph = builder.compile(
    interrupt_before=["tools"]  # 执行 tools 前暂停
)

# ========== 6. 运行（流式 + 人工确认） ==========

if __name__ == "__main__":

    print("=" * 60)
    print("Human-in-the-loop 测试")
    print("=" * 60)

    # 初始输入
    inputs = {
        "messages": [{"role": "user", "content": "帮我删除用户表中id=5的数据"}]
    }

    # 第一次运行：LLM思考 → 生成tool_calls → 在tools前中断
    for event in graph.stream(inputs, stream_mode="values"):
        last_msg = event["messages"][-1]
        last_msg_content = getattr(last_msg, "content", None) or last_msg.get("content", "")
        print(f"\n🤖 Agent: {last_msg_content[:80]}...")

        # 检查是否有tool_calls（说明要执行工具，已暂停）
        if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
            print(f"\n⚠️  即将执行以下操作：")
            for tc in last_msg.tool_calls:
                print(f"   工具: {tc['name']}")
                print(f"   参数: {tc['args']}")

            # 人工确认
            confirm = input("\n是否执行？[yes/no]: ").strip().lower()

            if confirm == "yes":
                # 继续执行：传入None，恢复中断
                print("\n✅ 继续执行...")

                initial_input = {
                    "messages": [("user", "你好，请介绍一下你自己")]
                }
                for event in graph.stream(initial_input, stream_mode="values"):
                    msg = event["messages"][-1]
                    if hasattr(msg, "tool_calls") and msg.tool_calls:
                        print(f"🛠️  执行工具: {msg.tool_calls[0]['name']}")
                    else:
                        msg_content = getattr(msg, "content", None)
                        safe_content = msg_content or "(无文本内容)"
                        print(f"📤 结果: {safe_content[:100]}...")
            else:
                print("\n❌ 已取消")
                break

    print("\n" + "=" * 60)
    print("测试2：安全操作（查询，无需确认也会经过中断点）")
    print("=" * 60)

    inputs2 = {
        "messages": [{"role": "user", "content": "查询一下今天的数据"}]
    }

    for event in graph.stream(inputs2, stream_mode="values"):
        last_msg = event["messages"][-1]
        last_msg_content = getattr(last_msg, "content", None)
        safe_content = last_msg_content or "(无文本内容)"
        print(f"\n🤖 Agent: {safe_content[:80]}...")

        if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
            print(f"\n⚠️  即将执行：{last_msg.tool_calls[0]['name']}")
            confirm = input("\n是否执行？[yes/no]: ").strip().lower()

            if confirm == "yes":
                for event in graph.stream(initial_input, stream_mode="values"):
                    msg = event["messages"][-1]
                    msg_content = getattr(msg, "content", None)
                    safe_content = msg_content or "(无文本内容)"
                    print(f"📤 结果: {safe_content[:100]}...")
            else:
                print("❌ 已取消")
                break