from datetime import date, datetime

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import (
    declared_attr, DeclarativeBase, Mapped, mapped_column)

from .constants import MAX_STR_LEN


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls):
        return f'{cls.__name__.lower()}s'

    id: Mapped[int] = mapped_column(primary_key=True)


class Author(Base):

    first_name: Mapped[str] = mapped_column(String(MAX_STR_LEN))
    last_name: Mapped[str] = mapped_column(String(MAX_STR_LEN))
    birth_date: Mapped[date]


class Book(Base):

    name: Mapped[str] = mapped_column(String(MAX_STR_LEN), unique=True)
    description: Mapped[str] = mapped_column(Text)
    author: Mapped[int] = mapped_column(
        ForeignKey(
            'authors.id',
            ondelete='CASCADE'
        )
    )
    available_books: Mapped[int]


class Borrow(Base):

    book: Mapped[int] = mapped_column(
        ForeignKey(
            'books.id',
            ondelete='RESTRICT'
        )
    )
    reader_name: Mapped[str]
    issue_date: Mapped[datetime | None] = mapped_column(
        server_default=func.now()
    )
    return_date: Mapped[date | None]
