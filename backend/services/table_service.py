from sqlalchemy.orm import Session
from backend.models.table import Table


def get_all_tables(db: Session):
    tables = db.query(Table).all()
    return tables