"""
FastAPI 查询参数练习
课程：黑马 FastAPI 07
"""

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/news/news_list")
async def get_news_list(
    skip: int = Query(0, description="跳过的记录数", lt=100),
    limit: int = Query(10, description="返回的记录数")
):
    """查询参数 + 分页"""
    return {"skip": skip, "limit": limit}


# 练习：图书查询
@app.get("/books")
async def get_books(
    category: str = Query("Python开发", min_length=5, max_length=255),
    price: int = Query(..., ge=50, le=100)
):
    """图书查询"""
    return {"图书分类": category, "价格": price}