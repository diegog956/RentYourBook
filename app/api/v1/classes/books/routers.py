from fastapi import APIRouter, Depends, status
from app.api.v1.classes.books import service
from app.api.v1.classes.books.schemas import BookInfo
from app.api.v1.database.database import get_db
from sqlalchemy.orm import Session

book_router = APIRouter()


@book_router.get('/', response_model=list[BookInfo], status_code=status.HTTP_200_OK)
async def get_books(page:int = 1, size: int = 10, db: Session = Depends(get_db)): #Esto es un query parameter, en dir: htt..../page=1?size=10
    #Llamar a servicio para mostrar los libros.

    libros : list[BookInfo] = service.get_books(page, size, db)   

    return libros