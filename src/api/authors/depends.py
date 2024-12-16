from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Author
from . import crud
from settings.db_helper import db_helper


async def get_author_by_id(
    id: int,
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Author:
    author = await crud.get_author(session, id)
    if author is not None:
        return author
    raise HTTPException(status.HTTP_404_NOT_FOUND)
