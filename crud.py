from sqlalchemy.orm import Session

import models, schema

#funciones de usuario

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_usuario(db: Session, usuario: str):
    return db.query(models.User).filter(models.User.usuario == usuario).first()

def get_user_by_telefono(db: Session, telefono: str):
    return db.query(models.User).filter(models.User.telefono == telefono).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#funciones de mock
def get_mock(db: Session, mock_id: int):
    return db.query(models.mock).filter(models.mock.id == mock_id).first()

def get_mock_by_codigo(db: Session, codigo: str):
    return db.query(models.mock).filter(models.mock.codigo == codigo).first()

def get_mock_by_url(db: Session, url: str):
    return db.query(models.mock).filter(models.mock.url == url).first()

def get_mock_by_metodo(db: Session, metodo: str):
    return db.query(models.mock).filter(models.mock.metodo == metodo).first()

def get_mock(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.mock).offset(skip).limit(limit).all()
    
def create_mock(db: Session, mock: schema.mock):
    db_mock = models.mock(codigo=mock.codigo, url=mock.url, metodo=mock.metodo)
    db.add(db_mock)
    db.commit()
    db.refresh(db_mock)
    return db_mock
