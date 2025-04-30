from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.dependencies.db import get_db
from backend.schemas.reservation import ReservationOut
from typing import List
from backend.services.reservation_service import get_all_reservations

router_reservation = APIRouter()

@router_reservation.get("/get_reservations", response_model=List[ReservationOut])
def get_reservations(db: Session = Depends(get_db)):
    return get_all_reservations(db)