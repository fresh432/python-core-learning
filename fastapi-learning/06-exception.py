"""
FastAPI 异常处理练习
课程：黑马 FastAPI 14
"""

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/news/{id}")
async def get_news(id: int):
    """异常处理：新闻不存在"""
    id_list = [1, 2, 3, 4, 5, 6]

    if id not in id_list:
        raise HTTPException(status_code=404, detail="您查找的新闻不存在")

    return {"id": id}