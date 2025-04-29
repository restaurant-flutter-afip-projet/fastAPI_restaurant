from sqlalchemy import Column, Integer, String, Float
from backend.db.base_class import Base

class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    price = Column(Float(), nullable=False)
    img_url = Column(String(300), nullable=False)
    category = Column(String(100), nullable=False)