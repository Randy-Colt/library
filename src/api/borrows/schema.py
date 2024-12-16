from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from core.constants import ConstrainedStr


class BorrowCreate(BaseModel):
    book: int
    reader_name: ConstrainedStr


class BorrowClose(BaseModel):
    return_date: date


class BorrowRetrieve(BorrowCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    issue_date: datetime
    return_date: date | None
