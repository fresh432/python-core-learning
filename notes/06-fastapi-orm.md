# FastAPI ORM 学习笔记（16-29集）

## 今日进度
- [x] 16 依赖注入：Depends 复用逻辑
- [x] 17 ORM 简介及安装：SQLAlchemy + aiomysql
- [x] 18 ORM 建表：DeclarativeBase + Mapped
- [x] 19 路由中使用数据库：依赖注入获取 Session
- [x] 20-23 查询操作：select、条件、聚合、分页
- [x] 24 分页查询
- [x] 26 新增数据
- [x] 27 更新数据
- [x] 28 删除数据
- [x] 29 ORM 总结

## 核心概念

### 1. 依赖注入
```python
async def common_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/items")
async def read_items(params=Depends(common_params)):
    return params
```
### 2. ORM 建表
```python
class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True)
    bookname: Mapped[str] = mapped_column(String(255))
```
### 3. 异步引擎
```python
async_engine = create_async_engine(
    "mysql+aiomysql://user:pass@localhost/db",
    echo=True,
    pool_size=10
)
```
### 4. 数据库会话
```python
AsyncSessionLocal = async_sessionmaker(bind=async_engine)

async def get_database():
    async with AsyncSessionLocal() as session:
        yield session
        await session.commit()
```
### 5. 查询操作
```python
# 查询所有
result = await db.execute(select(Book))
books = result.scalars().all()

# 条件查询
result = await db.execute(select(Book).where(Book.price > 50))

# 聚合
result = await db.execute(select(func.count(Book.id)))
```
### 6. 新增、更新、删除
```python
# 新增
db.add(book)
await db.commit()

# 更新
book.price = 99
await db.commit()

# 删除
await db.delete(book)
await db.commit()
```

## 注意事项
- __tablename__：不是 __table__，拼写错误会导致找不到表
- mapped_column：新版 SQLAlchemy 用法，旧版是 Column
- scalars().all()：异步查询结果需要这样获取，不是直接 result.all()