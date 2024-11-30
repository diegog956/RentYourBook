from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DATETIME, BINARY
from sqlalchemy.dialects.mysql import BINARY as MySQLBinary

Base = declarative_base()

class BookReturned(Base):
    __tablename__ = 'Books_Returned'

    id_records: int = Column(Integer, nullable=False, primary_key=True)
    id_user: BINARY = Column(MySQLBinary, nullable=False)
    id_book_unit = Column(Integer, nullable=False)
    date_take = Column(DATETIME)
    return_date = Column(DATETIME, nullable=False)

