"""
FastAPI 响应类型练习
课程：黑马 FastAPI 10-13
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel

app = FastAPI()


class News(BaseModel):
    """新闻模型"""
    id: int
    title: str
    content: str


@app.get("/html", response_class=HTMLResponse)
async def get_html():
    """返回 HTML"""
    return "<h1>这是一级标题</h1>"


@app.get("/file")
async def get_file():
    """返回文件"""
    file_path = "./files/1.jpeg"
    return FileResponse(file_path)


@app.get("/news/{id}", response_model=News)
async def get_news(id: int):
    """返回 JSON + 模型验证"""
    return {
        "id": id,
        "title": f"这是第{id}本书",
        "content": "这是一本好书"
    }