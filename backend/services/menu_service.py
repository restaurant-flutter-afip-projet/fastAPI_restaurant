from backend.models.menu import Dish
from sqlalchemy.orm import Session

def get_all_dishes(db: Session):
    dishes = db.query(Dish).all()
    return dishes