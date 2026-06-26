"""
FastAPI ORM 查询操作练习
课程：20-23集
要点：select、条件查询、聚合、分页
"""

from sqlalchemy import select, func, and_, or_
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, Integer
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    bookname: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Float)
    publisher: Mapped[str] = mapped_column(String(255))


# 查询所有
# result = await db.execute(select(Book))
# books = result.scalars().all()

# 条件查询：价格大于50
# result = await db.execute(select(Book).where(Book.price > 50))

# 多条件：价格大于50 且 作者是"张三"
# result = await db.execute(
#     select(Book).where(and_(Book.price > 50, Book.author == "张三"))
# )

# 聚合查询：统计数量
# result = await db.execute(select(func.count(Book.id)))
# count = result.scalar()

# 聚合查询：平均价格
# result = await db.execute(select(func.avg(Book.price)))
# avg_price = result.scalar()

# 分页查询
# result = await db.execute(select(Book).offset(10).limit(5))
# books = result.scalars().all()

# 排序
# result = await db.execute(select(Book).order_by(Book.price.desc()))


print("查询模板已定义")
print("使用时取消注释，在路由中调用")