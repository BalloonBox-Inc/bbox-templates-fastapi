'''This module defines general database CRUD operations.'''

from typing import Any
from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from apis.exceptions import ExceptionFormatter, exc


def create_object(db: Session, object: object):
    '''
    Add an object to the database.

        :param db [generator]: Database session.
        :param object [orm]: Declarative base object.

        :raises [HTTPException]:
            :[409] Conflict: Unable to add object to database.
    '''
    try:
        db.add(object)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        db.close()
        raise ExceptionFormatter(
            status_code=status.HTTP_409_CONFLICT,
            message=exc.DB_CREATE_OBJECT) from e


def get_object(db: Session, table: object, column: object, value: Any):
    '''
    Fetch database object if exists [1 condition].

        :param db [generator]: Database session.
        :param table [orm]: Declarative base Table.
        :param column [orm]: Declarative base Column.
        :param value: Value to look up.

        :returns: Database object.
    '''
    return db.query(table).filter(column == value).first()


def get_objects(db: Session, table: object, column: object, value: Any):
    '''
    Fetch all database objects if exist [1 condition].

        :param db [generator]: Database session.
        :param table [orm]: Declarative base Table.
        :param column [orm]: Declarative base Column.
        :param value: Value to look up.

        :returns: Database object.
    '''
    return db.query(table).filter(column == value).all()


def update_object(db: Session, object: object):  # pylint: disable=[W0613]
    '''
    Update a database object.

        :param db [generator]: Database session.
        :param object [orm]: Declarative base object.

        :raises [HTTPException]:
            :[409] Conflict: Unable to update object on database.
    '''
    try:
        db.flush()
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        db.close()
        raise ExceptionFormatter(
            status_code=status.HTTP_409_CONFLICT,
            message=exc.DB_UPDATE_OBJECT) from e


def delete_object(db: Session, object: object):
    '''
    Delete a database object.

        :param db [generator]: Database session.
        :param object [orm]: Declarative base object.

        :raises [HTTPException]:
            :[409] Conflict: Unable to delete object from database.
    '''
    try:
        db.delete(object)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        db.close()
        raise ExceptionFormatter(
            status_code=status.HTTP_409_CONFLICT,
            message=exc.DB_DELETE_OBJECT) from e
