from fastapi import APIRouter, Depends, status
from app.api.v1.classes.books import service
from app.api.v1.classes.books.schemas import BookInfo, BookAdd
from app.api.v1.database.database import get_db
from sqlalchemy.orm import Session
from app.api.v1.auth.authentication import verify_admin_access

book_router = APIRouter()


@book_router.get('/', response_model=list[BookInfo], status_code=status.HTTP_200_OK)
async def get_books(page:int = 1, size: int = 10, db: Session = Depends(get_db)): #Esto es un query parameter, en dir: htt..../page=1?size=10
    '''Muestra catalogo de libros. Por default Pagina = 1, Cantidad = 10'''

    libros : list[BookInfo] = service.get_books(page, size, db)   

    return libros

@book_router.get('/{id}', response_model=BookInfo, status_code=status.HTTP_200_OK)
async def get_book(id: int, db: Session = Depends(get_db)):
    '''Retorna una obra literaria por su ID.'''

    libro: BookInfo = service.get_book(id, db)
    
    return libro

@book_router.post('/', response_model=BookInfo, status_code=status.HTTP_201_CREATED, dependencies=[Depends(verify_admin_access)])
async def add_book(book: BookAdd, db:Session = Depends(get_db)):
    '''Agrega una obra literaria a la coleccion.'''

    book: BookInfo = service.add_book(book=book, db=db)
    
    return book

@book_router.delete('/{id}', response_model=BookInfo, status_code=status.HTTP_200_OK, dependencies=[Depends(verify_admin_access)])
async def delete_book(id:int, db: Session = Depends(get_db)):
    '''Elimina una obra literaria por su ISBN'''

    return service.delete_book(id, db)