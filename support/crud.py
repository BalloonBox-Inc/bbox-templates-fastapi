from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import exc
from support import models, schemas, hashing


def create_admin_user(db: Session, item: schemas.AdminCreate):
    new_admin_user = models.AdminTable(
        email=item.email, hashed_password=hashing.encrypt_password(item.password))
    try:
        db.add(new_admin_user)
        db.commit()
        db.refresh(new_admin_user)
    except Exception as e:
        db.rollback()
        db.close()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e))
    return new_admin_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.UserTable).filter(models.UserTable.email == email).first()


def add_row(db: Session, obj: models.UserTable):
    try:
        db.add(obj)
        db.commit()
        return
    except exc.SQLAlchemyError:
        db.rollback()
        db.close()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Unable to add data to database')


def update_row(db: Session, obj: models.UserTable):
    try:
        db.flush()
        db.commit()
        return
    except exc.SQLAlchemyError:
        db.rollback()
        db.close()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Unable to update data to database')
