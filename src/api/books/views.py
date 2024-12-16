from typing import Sequence

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .depends import get_book_by_id
from .schema import BookCreateOrUpdate, BookRetrieve
from core.models import Book
from settings.db_helper import db_helper

router = APIRouter(prefix='/books', tags=['books'])


@router.get('/', response_model=list[BookRetrieve])
async def get_books(
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Sequence[Book]:
    return await crud.get_books(session)


@router.post(
        '/',
        response_model=BookRetrieve,
        status_code=status.HTTP_201_CREATED
)
async def post_book(
    kwargs: BookCreateOrUpdate,
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Book:
    return await crud.create_book(session, kwargs)


@router.get('/{id}', response_model=BookRetrieve)
async def get_book(
    id: int,
    book: Book = Depends(get_book_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Book:
    return book


@router.put('/{id}', response_model=BookRetrieve)
async def update_book(
    id: int,
    kwargs: BookCreateOrUpdate,
    book: Book = Depends(get_book_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Book:
    return await crud.update_book(session, book, kwargs)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    id: int,
    book: Book = Depends(get_book_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> None:
    await crud.delete_book(session, book)
