from pydantic import BaseModel, ConfigDict, PastDate

from core.constants import ConstrainedStr


class AuthorCreateOrUpdate(BaseModel):
    first_name: ConstrainedStr
    last_name: ConstrainedStr
    birth_date: PastDate


class AuthorRetrieve(AuthorCreateOrUpdate):
    model_config = ConfigDict(from_attributes=True)
    id: int
