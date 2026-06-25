"""
FastAPI 路径参数练习
课程：黑马 FastAPI 04-06
"""

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/book/{id}")
async def get_book(
    id: int = Path(..., gt=0, le=100, description="书籍id, 取值范围1-100")
):
    """路径参数 + 范围验证"""
    return {"id": id, "title": f"这是第{id}本书"}


@app.get("/author/{name}")
async def get_author(
    name: str = Path(..., min_length=2, max_length=10)
):
    """路径参数 + 长度验证"""
    return {"msg": f"这是{name}的信息"}


# 练习：新闻分类
@app.get("/news_id/{news_id}")
async def get_news_id(
    news_id: int = Path(..., gt=0, le=100)
):
    """新闻ID"""
    return {"msg": f"news_id为{news_id}"}


@app.get("/news_name/{news_name}")
async def get_news_name(
    news_name: str = Path(..., min_length=2, max_length=10)
):
    """新闻名称"""
    return {"msg": f"news_name为{news_name}"}