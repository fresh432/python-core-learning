"""
结构化输出测试
- 强制 JSON 输出，方便后端解析
- Pydantic 约束字段
"""

import os
import json
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)


class ArticleSummary(BaseModel):
    title: str
    summary: str
    keywords: list[str]


def structured_chat():
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "你是一个文章摘要助手，请用JSON格式输出，包含title、summary、keywords字段",
            },
            {
                "role": "user",
                "content": "请为以下文章生成摘要和关键词：FastAPI是一个现代、高性能的Python Web框架...",
            },
        ],
        response_format={"type": "json_object"},
    )

    result = json.loads(response.choices[0].message.content)
    summary = ArticleSummary(**result)
    print(f"标题: {summary.title}")
    print(f"摘要: {summary.summary}")
    print(f"关键词: {summary.keywords}")


if __name__ == "__main__":
    structured_chat()