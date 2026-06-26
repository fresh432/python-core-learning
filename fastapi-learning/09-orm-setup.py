"""
FastAPI ORM 配置练习
课程：17集
要点：创建引擎、连接池配置
"""

from sqlalchemy.ext.asyncio import create_async_engine

# 异步 MySQL 引擎（需要本地 MySQL 服务）
ASYNC_DATABASE_URL = "mysql+aiomysql://root:123456@localhost:3306/fastapi_first?charset=utf8"

async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,           # 输出 SQL 日志，调试用
    pool_size=10,        # 连接池活跃连接数
    max_overflow=20      # 允许额外的连接数
)

# 同步 SQLite 引擎（项目用，无需安装 MySQL）
from sqlalchemy import create_engine

sync_engine = create_engine(
    "sqlite:///./test.db",
    connect_args={"check_same_thread": False}
)

print("引擎创建成功")
print(f"异步引擎: {async_engine}")
print(f"同步引擎: {sync_engine}")