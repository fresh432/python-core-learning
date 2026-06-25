"""
FastAPI 请求体参数练习
课程：黑马 FastAPI 08-09
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    """用户模型"""
    username: str = Field(
        default="张三",
        min_length=2,
        max_length=10,
        description="用户名, 长度要求2-10个字"
    )
    password: str = Field(min_length=3, max_length=20)


@app.post("/register")
async def register(user: User):
    """用户注册"""
    return user


# 练习：图书模型
class Book(BaseModel):
    """图书模型"""
    title: str = Field(..., min_length=2, max_length=20)
    author: str = Field(min_length=2, max_length=10)
    publisher: str = Field(default="黑马出版社")
    price: float = Field(gt=0)


@app.post("/add_book")
async def add_book(book: Book):
    """添加图书"""
    return book