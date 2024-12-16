from typing import Sequence

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schema import AuthorCreateOrUpdate
from core.models import Author


async def get_authors(session: AsyncSession) -> Sequence[Author]:
    result: Result = await session.execute(select(Author))
    return result.scalars().all()


async def get_author(session: AsyncSession, id: int) -> Author | None:
    return await session.get(Author, id)


async def create_author(session: AsyncSession, kwargs: AuthorCreateOrUpdate) -> Author:
    author = Author(**kwargs.model_dump())
    session.add(author)
    await session.commit()
    return author


async def update_author(
        session: AsyncSession,
        author: Author,
        kwargs: AuthorCreateOrUpdate
) -> Author:
    for name, value in kwargs.model_dump().items():
        setattr(author, name, value)
    await session.commit()
    return author


async def delete_author(
        session: AsyncSession,
        author: Author
) -> None:
    await session.delete(author)
    await session.commit()
