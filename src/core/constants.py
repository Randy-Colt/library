from typing import Annotated

from pydantic import StringConstraints


MAX_STR_LEN = 30
MIN_STR_LEN = 1


ConstrainedStr = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=MIN_STR_LEN,
        max_length=MAX_STR_LEN
    )
]
