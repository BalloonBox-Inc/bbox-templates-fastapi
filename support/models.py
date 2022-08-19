from sqlalchemy import Column, Boolean, Integer, Float, String, DateTime
from support.database import Base


class UserTable(Base):

    __tablename__ = 'users_test'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
