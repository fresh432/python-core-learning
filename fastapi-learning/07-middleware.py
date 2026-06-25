"""
FastAPI 中间件练习
课程：黑马 FastAPI 15
"""

from fastapi import FastAPI

app = FastAPI()


@app.middleware("http")
async def middleware1(request, call_next):
    """中间件1"""
    print("中间件1 start")
    response = await call_next(request)
    print("中间件1 end")
    return response


@app.middleware("http")
async def middleware2(request, call_next):
    """中间件2"""
    print("中间件2 start")
    response = await call_next(request)
    print("中间件2 end")
    return response


@app.get("/")
async def root():
    """测试中间件的路由"""
    print("处理请求")
    return {"message": "Hello World"}