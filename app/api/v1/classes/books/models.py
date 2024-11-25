from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Date

Base = declarative_base()


class Books(Base):

    __tablename__ = 'Books'

    id_book: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable=False)
    release_year: Date = Column(Date, nullable=False)
    favorites_amount:int = Column(Integer, default=0 ,nullable=False)
    available_units: int = Column(Integer, default=1, nullable=False)
    image_url: str = Column(String, nullable=True)
    #Añadir Relationships entre tablas.



