"""
LLM 原生 API 调用测试
- 非流式：一次返回完整响应
- 流式：SSE 逐字返回
"""

import os
from openai import OpenAI

# DeepSeek API（OpenAI 兼容格式）
client = OpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)


def chat_non_stream():
    """非流式调用"""
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个技术博客助手"},
            {"role": "user", "content": "请用一句话介绍FastAPI框架"},
        ],
        temperature=0.7,
        max_tokens=200,
    )
    print("非流式输出：")
    print(response.choices[0].message.content)


def chat_stream():
    """流式调用（SSE）"""
    stream = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": "请介绍Python装饰器"}],
        stream=True,
    )
    print("流式输出：")
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()


if __name__ == "__main__":
    chat_non_stream()
    print("-" * 40)
    chat_stream()