from pydantic import BaseModel, Field
from enum import IntEnum
from pydantic.error_wrappers import Optional


class StatusChoices(IntEnum):
    success = 0
    fail = 1


class Response(BaseModel):
    status: StatusChoices = StatusChoices.fail
    data: Optional[BaseModel] = None
    reason: str = None

