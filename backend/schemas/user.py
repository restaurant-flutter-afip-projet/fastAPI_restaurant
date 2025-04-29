from pydantic import BaseModel, constr

class User(BaseModel):
    id : int
    firstname: str
    lastname: str
    email : str
    phone_number : str
    password: str
    role: str

class UserOut(User):
    id: int

    class Config:
        from_attributes = True