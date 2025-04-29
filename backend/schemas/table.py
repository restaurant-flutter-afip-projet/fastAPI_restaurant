from pydantic import BaseModel, conint

class Table(BaseModel):
    id: int
    capacity: int

class TableOut(Table):
    id: int

    class Config:
        from_attributes = True