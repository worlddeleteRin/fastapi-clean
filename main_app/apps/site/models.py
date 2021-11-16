import uuid
from typing import Optional

from pydantic import UUID4, BaseModel, Field

# from database.main_db import db_provider


class SomeModelName(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    info: Optional[str]

    class Config:
        allow_population_by_field_name = True

