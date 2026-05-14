# BaseModel Pydantic
from pydantic import BaseModel


# Création utilisateur
class UserCreate(BaseModel):

    username: str
    email: str
    password: str
    role: str


# Réponse utilisateur
class UserResponse(BaseModel):

    id: int
    username: str
    email: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True