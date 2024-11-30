from sqlalchemy.orm import Session
from .schemas import BookReturnedInfo
from .models import BookReturned
from uuid import UUID
from fastapi import HTTPException, status


def get_all_old_records(amount:int, db: Session):
    
    lista: list[BookReturnedInfo] = db.query(BookReturned).limit(amount).all()
    
    if not lista:
    
        raise HTTPException(detail='Records not found.', status_code=status.HTTP_404_NOT_FOUND)
    
    return lista

def get_old_records_by_id(id: UUID, db:Session):

    lista: list[BookReturnedInfo] = db.query(BookReturned).filter(BookReturned.id_user == id.bytes).all()
    
    if not lista:

        raise HTTPException(detail='Records not found for id provided.', status_code=status.HTTP_404_NOT_FOUND)
    
    return lista