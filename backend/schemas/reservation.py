from pydantic import BaseModel, conint
from datetime import datetime


class Reservation(BaseModel):
    id : int
    user_id : int
    table_id : int
    datetime: datetime
    peopleNbr: int

class ReservationOut(Reservation):
    id: int

    class Config:
        from_attributes = True
