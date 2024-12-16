from pydantic import BaseModel, ConfigDict, NonNegativeInt

from core.constants import ConstrainedStr


class BookCreateOrUpdate(BaseModel):
    name: ConstrainedStr
    description: str
    author: int
    available_books: NonNegativeInt


class BookRetrieve(BookCreateOrUpdate):
    model_config = ConfigDict(from_attributes=True)
    id: int
