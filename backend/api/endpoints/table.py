from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.dependencies.db import get_db
from backend.schemas.table import TableOut
from typing import List
from backend.services.table_service import get_all_tables

router_table = APIRouter()

@router_table.get("/get_tables", response_model=List[TableOut])
def get_tables(db: Session = Depends(get_db)):
    return get_all_tables(db)