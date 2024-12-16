from typing import Sequence

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .depends import get_borrow_by_id
from .schema import BorrowClose, BorrowCreate, BorrowRetrieve
from core.models import Borrow
from core.services import (
    check_available_book, check_book_exists, increment_books_count, decrement_books_count
)
from settings.db_helper import db_helper

router = APIRouter(prefix='/borrows', tags=['borrows'])


@router.get('/', response_model=list[BorrowRetrieve])
async def get_borrows(
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Sequence[Borrow]:
    return await crud.get_borrows(session)


@router.post(
    '/',
    response_model=BorrowRetrieve,
    status_code=status.HTTP_201_CREATED
)
async def post_borrow(
    kwargs: BorrowCreate,
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Borrow:
    if await check_book_exists(session, kwargs.book) is None:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            'This book does not exist'
        )
    if await check_available_book(session, kwargs.book):
        await decrement_books_count(session, kwargs.book)
        return await crud.create_borrow(session, kwargs)
    raise HTTPException(
        status.HTTP_422_UNPROCESSABLE_ENTITY,
        'No books available'
    )


@router.get('/{id}', response_model=BorrowRetrieve)
async def get_borrow(
    id: int,
    borrow: Borrow = Depends(get_borrow_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Borrow:
    return borrow


@router.patch('/{id}', response_model=BorrowRetrieve)
async def close_borrow(
    id: int,
    kwargs: BorrowClose,
    borrow: Borrow = Depends(get_borrow_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Borrow:
    await increment_books_count(session, borrow.book)
    return await crud.close_borrow(session, borrow, kwargs)
