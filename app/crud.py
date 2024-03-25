from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, email: str, user_data: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if db_user:
        for key, value in user_data.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, email: str):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
