from typing import Sequence

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .depends import get_author_by_id
from .schema import AuthorCreateOrUpdate, AuthorRetrieve
from core.models import Author
from settings.db_helper import db_helper

router = APIRouter(prefix='/authors', tags=['authors'])


@router.get('/', response_model=list[AuthorRetrieve])
async def get_authors(
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Sequence[Author]:
    return await crud.get_authors(session)


@router.post(
    '/',
    response_model=AuthorRetrieve,
    status_code=status.HTTP_201_CREATED
)
async def post_author(
    kwargs: AuthorCreateOrUpdate,
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Author:
    return await crud.create_author(session, kwargs)


@router.get('/{id}', response_model=AuthorRetrieve)
async def get_author(
    id: int,
    author: Author = Depends(get_author_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Author:
    return author


@router.put('/{id}', response_model=AuthorRetrieve)
async def update_author(
    id: int,
    kwargs: AuthorCreateOrUpdate,
    author: Author = Depends(get_author_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Author:
    return await crud.update_author(session, author, kwargs)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(
    id: int,
    author: Author = Depends(get_author_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> None:
    await crud.delete_author(session, author)
