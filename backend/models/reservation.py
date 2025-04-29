from sqlalchemy import Column, Integer, ForeignKey, DateTime
from backend.db.base_class import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)
    datetime = Column(DateTime, nullable=False)
    people_nbr = Column(Integer, nullable=False)