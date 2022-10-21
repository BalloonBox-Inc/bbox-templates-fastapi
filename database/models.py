'''This module defines all database tables.'''

from sqlalchemy import Column, Boolean, Integer, String, DateTime
from sqlalchemy.sql import func
from database.session import Base


class UserTable(Base):
    '''Define users as a database table.'''

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    blockchain = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
