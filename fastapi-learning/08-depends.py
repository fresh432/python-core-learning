"""
FastAPI 依赖注入练习
课程：16集
要点：Depends 复用逻辑，如分页参数
"""

from fastapi import FastAPI, Query, Depends

app = FastAPI()


# 共用分页参数
async def common_parameters(
    skip: int = Query(0, ge=0, description="跳过的记录数"),
    limit: int = Query(10, le=60, description="返回的记录数")
):
    return {"skip": skip, "limit": limit}


# 新闻列表 - 使用依赖注入
@app.get("/news/news_list")
async def get_news_list(commons=Depends(common_parameters)):
    return commons


# 用户列表 - 复用同一分页逻辑
@app.get("/user/user_list")
async def get_user_list(commons=Depends(common_parameters)):
    return commons


# 练习：自定义依赖
async def verify_token(token: str = Query(...)):
    if token != "valid":
        raise ValueError("无效token")
    return {"token": token}


@app.get("/secure")
async def secure_route(auth=Depends(verify_token)):
    return {"message": "验证通过", "auth": auth}