from typing import Sequence

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schema import BorrowClose, BorrowCreate
from core.models import Borrow


async def get_borrows(session: AsyncSession) -> Sequence[Borrow]:
    result: Result = await session.execute(select(Borrow))
    return result.scalars().all()


async def get_borrow(session: AsyncSession, id: int) -> Borrow | None:
    return await session.get(Borrow, id)


async def create_borrow(
        session: AsyncSession,
        kwargs: BorrowCreate
) -> Borrow:
    borrow = Borrow(**kwargs.model_dump())
    session.add(borrow)
    await session.commit()
    return borrow


async def close_borrow(
    session: AsyncSession,
    borrow: Borrow,
    kwargs: BorrowClose
) -> Borrow:
    borrow.return_date = kwargs.return_date
    await session.commit()
    return borrow
