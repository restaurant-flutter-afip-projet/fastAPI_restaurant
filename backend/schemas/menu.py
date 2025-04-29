from pydantic import BaseModel

class Dish(BaseModel):
    id: int
    name: str
    description: str
    price: float
    img_url: str
    category: str

class DishOut(Dish):
    id: int

    class Config:
        from_attributes = True


