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
        raise HTTPException(detail='Pagination out of bounds.', status_code=status.HTTP_204_NO_CONTENT)

    return lista