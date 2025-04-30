from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.dependencies.db import get_db
from backend.schemas.menu import DishOut
from typing import List
from backend.services.menu_service import get_all_dishes

router_menu = APIRouter()

@router_menu.get("/get_menu", response_model=List[DishOut])
def get_menu(db: Session = Depends(get_db)):
    return get_all_dishes(db)