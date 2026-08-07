"""
Agent实战：真实LLM + Tool Calling
- 使用OpenAI格式调用真实LLM
- LLM自己决定调用哪个工具
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

# 定义工具
@tool
def search(query: str) -> str:
    """搜索工具，用于查询天气、新闻等实时信息"""
    return f"搜索结果：{query} 的相关信息..."


@tool
def calculate(expression: str) -> str:
    """计算工具，用于数学运算"""
    try:
        result = eval(expression)
        return f"计算结果：{result}"
    except:
        return "计算失败"


# LLM绑定工具
llm = ChatOpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    model="deepseek-chat",
)
llm_with_tools = llm.bind_tools([search, calculate])

# 调用：LLM会根据问题决定是否调用工具
response = llm_with_tools.invoke("北京天气怎么样？")
print(response)