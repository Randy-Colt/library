from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Borrow
from . import crud
from settings.db_helper import db_helper


async def get_borrow_by_id(
    id: int,
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Borrow:
    borrow = await crud.get_borrow(session, id)
    if borrow is not None:
        return borrow
    raise HTTPException(status.HTTP_404_NOT_FOUND)
