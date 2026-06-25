"""
FastAPI 基础路由练习
课程：黑马 FastAPI 01-03
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """根路由"""
    return {"message": "Hello World"}


@app.get("/hello")
async def hello():
    """Hello 路由"""
    return {"message": "你好 FastAPI"}


# 练习：自定义路由
@app.get("/user/hello")
async def user_hello():
    """用户路由"""
    return {"msg": "我正在学习FastAPI"}