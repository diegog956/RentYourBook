from app.api.v1.classes.books.schemas import BookAdd, BookInfo
from app.api.v1.database.database import get_db
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .models import Books

def get_books(page:int, size:int, db: Session) -> list[BookInfo]:
    
    offset = (page - 1) * size

    lista:list[BookInfo] = db.query(Books).offset(offset).limit(page).all()

    if lista is None: 
        raise HTTPException(detail='Pagination out of bounds.', status_code=status.HTTP_404_NOT_FOUND)

    return lista

def get_book(id:int, db: Session) -> BookInfo:

    book: BookInfo | None = db.query(Books).filter(Books.id_book == id).first()

    if book is None: 
        raise HTTPException(detail='Book not found in database.', status_code=status.HTTP_404_NOT_FOUND)

    return book

def add_book(book: BookAdd, db:Session) -> BookInfo:
    
    db_book: BookInfo = db.query(Books).filter(Books.id_book == book.id).first()
    if db_book is not None:
        raise HTTPException(detail='Book already added to database.', status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
    book_sql: Books = Books(**book.model_dump())

    db.add(book_sql)
    db.commit()
    #No realizo db.refresh() ya que no hago put ni patch.

    #Retorno book(Books) y fastapi se encarga de la conversion a BookInfo
    return book_sql

def delete_book(id: int , db: Session) -> BookInfo:

    book: Books | None = db.query(Books).filter(Books.id_book == id).first()
    if book is None:
        raise HTTPException(detail='Book not found in database.', status_code=status.HTTP_404_NOT_FOUND)    

    db.delete(book)
    db.commit()

    return book

def change_password(token:str, db:Session):
    pass