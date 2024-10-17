from sqlalchemy import Column, String, Boolean, Date, Enum, Integer
from sqlalchemy.dialects.mysql import BINARY as MySQLBinary
from sqlalchemy.orm import declarative_base
from uuid import UUID
from app.api.v1.utils.enums import Role


Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id_user = Column(MySQLBinary(16), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    verified_email = Column(Boolean, default=False, nullable=False)
    name = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    birthdate = Column(Date, nullable=False)
    user_role = Column(Enum(Role), nullable=False)
    warning_amounts = Column(Integer, default=0, nullable=False)
    ban = Column(Boolean, default=False, nullable=False)
    rented_books = Column(Integer, nullable=False)

