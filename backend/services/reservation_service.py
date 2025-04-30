from backend.models.reservation import Reservation
from sqlalchemy.orm import Session


def get_all_reservations(db: Session):
    reservations = db.query(Reservation).all()
    return reservations