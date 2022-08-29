from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import exc


def get_user_by_email(db: Session, user_model, email):
    return db.query(user_model).filter(user_model.email == email).first()


def create_user(db: Session, user_model):
    try:
        db.add(user_model)
        db.commit()
        return
    except exc.SQLAlchemyError as e:
        db.rollback()
        db.close()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Unable to add data into database') from e


def update_user(db: Session, user_model):
    try:
        db.flush()
        db.commit()
        return
    except exc.SQLAlchemyError as e:
        db.rollback()
        db.close()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Unable to update data to database') from e
