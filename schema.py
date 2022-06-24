from typing import List, Union

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    usuario: str
    telefono: str

   
class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class mock(BaseModel):
    id: int
    codigo: str
    url: str
    metodo: str 

    class Config:
        orm_mode = True
