from typing import Any, List
from pydantic import BaseModel


class SchemaRequest(BaseModel):
    object: str
    entry: List = []
