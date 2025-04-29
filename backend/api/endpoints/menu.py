from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.dependencies.db import get_db
from backend.schemas.menu import DishOut
from typing import List
from backend.models.menu import Dish

router_menu = APIRouter()


@router_menu.get("/get_menu", response_model=List[DishOut])  # Utilisez "/" pour représenter /api/menu
def get_menu(db: Session = Depends(get_db)):
    dishes = db.query(Dish).all()
    return dishes