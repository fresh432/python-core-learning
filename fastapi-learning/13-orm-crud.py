"""
FastAPI ORM 增删改练习
课程：26-28集
要点：add、修改、delete + commit
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, Float, Integer, select
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()


# 假设 Book 模型和 get_db 已定义


# ========== 新增（26集）==========
@app.post("/books")
async def create_book(
        book_data: dict,
        db: AsyncSession = Depends(lambda: None)  # 替换为实际的 get_db
):
    """新增书籍"""
    # 创建对象
    book = Book(**book_data)

    # 添加到会话
    db.add(book)

    # 提交事务
    await db.commit()

    # 刷新获取最新状态（如自动生成的id）
    await db.refresh(book)

    return book


# ========== 更新（27集）==========
@app.put("/books/{book_id}")
async def update_book(
        book_id: int,
        book_data: dict,
        db: AsyncSession = Depends(lambda: None)
):
    """更新书籍"""
    # 查询原对象
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalar_one_or_none()

    if not book:
        raise HTTPException(status_code=404, detail="书籍不存在")

    # 修改属性
    for key, value in book_data.items():
        setattr(book, key, value)

    # 提交
    await db.commit()
    await db.refresh(book)

    return book


# ========== 删除（28集）==========
@app.delete("/books/{book_id}")
async def delete_book(
        book_id: int,
        db: AsyncSession = Depends(lambda: None)
):
    """删除书籍"""
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalar_one_or_none()

    if not book:
        raise HTTPException(status_code=404, detail="书籍不存在")

    # 删除
    await db.delete(book)
    await db.commit()

    return {"message": "删除成功"}


# 同步版本（项目用）
def create_book_sync(db: Session, book_data: dict):
    """同步新增"""
    book = Book(**book_data)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book