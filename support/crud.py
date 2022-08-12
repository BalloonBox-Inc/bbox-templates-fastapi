from sqlalchemy.orm import Session
from support import models, schemas


def get_user_by_email(db: Session, email: str):
    return db.query(models.UserTable).filter(models.UserTable.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.UserTable(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
