"""
FastAPI ORM 模型定义练习
课程：18集
要点：DeclarativeBase、Mapped、mapped_column
"""

from datetime import datetime
from sqlalchemy import DateTime, func, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# 基类：包含创建时间、更新时间
class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(
        DateTime,
        insert_default=func.now(),
        default=func.now,
        comment="创建时间"
    )
    update_time: Mapped[datetime] = mapped_column(
        DateTime,
        insert_default=func.now(),
        default=func.now,
        onupdate=func.now(),
        comment="修改时间"
    )


# 书籍模型
class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍id")
    bookname: Mapped[str] = mapped_column(String(255), comment="书名")
    author: Mapped[str] = mapped_column(String(255), comment="作者")
    price: Mapped[float] = mapped_column(Float, comment="价格")
    publisher: Mapped[str] = mapped_column(String(255), comment="出版社")


# 练习：用户模型
class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, comment="用户id")
    username: Mapped[str] = mapped_column(String(10), comment="用户名")
    password: Mapped[str] = mapped_column(String(255), comment="用户密码")


print(f"Book 表名: {Book.__tablename__}")
print(f"User 表名: {User.__tablename__}")