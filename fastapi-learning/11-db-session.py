"""
FastAPI 数据库会话练习
课程：19集
要点：async_sessionmaker、依赖注入获取会话
"""

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from fastapi import FastAPI, Depends

# 假设 async_engine 已创建（见 09-orm-setup.py）
# from sqlalchemy.ext.asyncio import create_async_engine
# async_engine = create_async_engine("...")

app = FastAPI()


# 会话工厂
AsyncSessionLocal = async_sessionmaker(
    # bind=async_engine,      # 绑定引擎（实际使用时取消注释）
    class_=AsyncSession,
    expire_on_commit=False     # 提交后会话不过期
)


# 依赖项：获取数据库会话
async def get_database():
    async with AsyncSessionLocal() as session:
        try:
            yield session          # 返回会话给路由
            await session.commit() # 提交事务
        except Exception:
            await session.rollback()  # 异常回滚
            raise
        finally:
            await session.close()     # 关闭会话


@app.get("/test-db")
async def test_db(db: AsyncSession = Depends(get_database)):
    """测试数据库连接"""
    return {"message": "数据库连接成功"}


# 同步版本（项目用）
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

sync_engine = create_engine("sqlite:///./test.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()