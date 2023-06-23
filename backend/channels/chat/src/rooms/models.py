from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator
# from utils.models import PydanticObjectId


class Room(BaseModel):
    """ Room model """
    index: Optional[str]
    created_at: datetime = Field(default=datetime.utcnow())
    updated_at: datetime = Field(default=datetime.utcnow())
    participiants: list

    @validator('participiants')
    def validate_room_name(cls, v):
        print(v)
        if isinstance(v, list):
            return v
        raise ValueError("participitants must be a list")

    @validator('created_at')
    def validate_created_at(cls, v):
        try:
            datetime.strptime(str(v), '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError as e:
            raise ValueError("Invalid created_at format. Expected format: YYYY-MM-DDTHH:MM:SS.sssZ") from e

        if v > datetime.utcnow():
            raise ValueError("created_at can't be in the future.")
        return v

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "created_at": "2023-04-22T12:00:00.000Z"
            }
        }

