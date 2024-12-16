from typing import Sequence

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schema import BookCreateOrUpdate
from core.models import Book


async def get_books(session: AsyncSession) -> Sequence[Book]:
    result: Result = await session.execute(select(Book))
    return result.scalars().all()


async def get_book(session: AsyncSession, id: int) -> Book | None:
    return await session.get(Book, id)


async def create_book(
        session: AsyncSession,
        kwargs: BookCreateOrUpdate
) -> Book:
    book = Book(**kwargs.model_dump())
    session.add(book)
    await session.commit()
    return book


async def update_book(
        session: AsyncSession,
        book: Book,
        kwargs: BookCreateOrUpdate
) -> Book:
    for name, value in kwargs.model_dump().items():
        setattr(book, name, value)
    await session.commit()
    return book


async def delete_book(
        session: AsyncSession,
        book: Book
) -> None:
    await session.delete(book)
    await session.commit()
