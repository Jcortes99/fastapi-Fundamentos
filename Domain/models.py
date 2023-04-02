from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
    name : str
    last_name : str
    age : int
    hair_colour: Optional[str] = None
    is_married: Optional[str] = None