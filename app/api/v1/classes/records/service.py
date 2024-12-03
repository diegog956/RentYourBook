from fastapi import HTTPException, status
from .models import Record
from sqlalchemy.orm import Session
from .schemas import RecordInfo, RecordAdd
from app.api.v1.auth.authentication import get_id
from app.api.v1.classes.books_returned.models import BookReturned
from app.api.v1.classes.books_returned.service import add_new_records_to_record_history
from app.api.v1.classes.books_returned.schemas import BookReturnedInfo
from app.api.v1.classes.users.service import get_amount_warnings, add_plus_one_rented_books

def get_all_records(db:Session) -> list[RecordInfo]:
    return db.query(Record).all()

def get_my_records(token:str, db:Session):
    id: bytes = get_id(token)
    return db.query(Record).filter(Record.id_user == id)

def add_record(record: RecordAdd, token:str, db:Session) -> RecordInfo:
    record_db: Record = Record(**record.model_dump())
    #Busco el id del usuario que quiere reservar un libro

    id: bytes = get_id(token, db)

    #Verifico que el usuario tenga menos de 3 reservas para poder reservar.

    if len(get_my_records(token, db)) > 2:
        raise HTTPException(detail='User already has 3 active reservations.', status_code=status.HTTP_403_FORBIDDEN)

    #Marco como False el campo available en book_unit.

    'Falta crear la entidad Book_Unit'

    #Sumo +1 en el campo 'Rented_Books' del usuario.
    
    add_plus_one_rented_books(id, db)

    # Si todo esta bien: Añado a la bdd y retorno la info del libro agregado.
    # (Quizas deberia de agregar el id de la unidad y no de la obra.)
    db.add(record_db)
    db.commit()
    db.refresh(record_db)
    return record_db

def delete_record(id_book_unit: int, db:Session)->BookReturnedInfo:

    '''
    Elimina el registro de la reserva cuando el cliente retorna el libro.
    Además, lo añade a la tabla de historial.
    '''

    #Tomo el registro a eliminar
    record_sql: Record = db.query(Record).filter(Record.id_book_unit == id_book_unit).first()
    
    #Creo el objeto BookReturned para agregar en tabla de historial
    bookreturned: BookReturned = BookReturned(**record_sql.__dict__, return_date=record_sql.expected_return_date)

    #Agrego en la tabla de libros retornados.
    add_new_records_to_record_history(bookreturned, db)

    #Retorno el Item de Historial
    return bookreturned