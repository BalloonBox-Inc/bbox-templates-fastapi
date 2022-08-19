from sqlalchemy.orm import Session
from support import models


def get_user_by_email(db: Session, email: str):
    return db.query(models.UserTable).filter(models.UserTable.email == email).first()


def add_row(db: Session, obj: models.UserTable):
    db.add(obj)
    db.commit()
    return


def update_row(db: Session, obj: models.UserTable):
    db.flush()
    db.commit()
    return
