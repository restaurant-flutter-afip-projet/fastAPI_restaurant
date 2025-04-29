from sqlalchemy import Column, Integer, String
from backend.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    phone_number = Column(String(10), nullable=False)
    password = Column(String(200), nullable=False)
    role = Column(String(30), nullable=False)