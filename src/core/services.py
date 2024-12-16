from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Book


async def check_available_book(
    session: AsyncSession,
    book_id: int
) -> bool:
    result: Result = await session.execute(
        select(Book.available_books).where(Book.id == book_id)
    )
    available_count = result.scalar_one()
    return available_count > 0


async def decrement_books_count(
    session: AsyncSession,
    book_id: int
) -> None:
    book = await session.get(Book, book_id)
    book.available_books -= 1
    await session.commit()


async def increment_books_count(
    session: AsyncSession,
    book_id: int
) -> None:
    book = await session.get(Book, book_id)
    book.available_books += 1
    await session.commit()


async def check_book_exists(
    session: AsyncSession,
    book_id: int
) -> Book | None:
    result: Result = await session.execute(
        select(Book.available_books).where(Book.id == book_id)
    )
    return result.scalar_one_or_none()
