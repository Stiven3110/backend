from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(32), unique=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)
    telefono = Column(String(15))
    usuario = Column(String(30))
    

class mock(Base):
    __tablename__ = "mocks"

    id = Column(Integer, primary_key=True)
    codigo = Column(String(100), unique=True)
    url = Column(String(1000))
    metodo = Column(String(10))


