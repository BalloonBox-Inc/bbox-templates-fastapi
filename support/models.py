from sqlalchemy import Column, Boolean, Integer, Float, String, DateTime, null
from support.database import Base


# database table classes
class AdminTable(Base):

    __tablename__ = 'admin_test'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


class UserTable(Base):

    __tablename__ = 'users_test'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
