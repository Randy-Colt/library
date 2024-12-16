from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Book
from . import crud
from settings.db_helper import db_helper


async def get_book_by_id(
    id: int,
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Book:
    book = await crud.get_book(session, id)
    if book is not None:
        return book
    raise HTTPException(status.HTTP_404_NOT_FOUND)
