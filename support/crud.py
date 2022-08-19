from sqlalchemy.orm import Session
from support import models


# fetch row by column value
def get_row_by_column(db: Session, value: str):
    return db.query(models.UserTable).filter(models.UserTable.email == value).first()


# fetch row where column is empty
def get_row_by_column_null(db: Session):
    return db.query(models.UserTable).filter(models.UserTable.email == None).order_by(models.UserTable.email.asc()).first()


# add new row
def add_row(db: Session, obj: models.UserTable):
    db.add(obj)
    db.commit()
    return


# update existent row
def update_row(db: Session, obj: models.UserTable):
    db.flush()
    db.commit()
    return
