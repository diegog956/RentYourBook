from .models import Record
from sqlalchemy.orm import Session
from .schemas import RecordInfo, RecordAdd
from app.api.v1.auth.authentication import get_id

def get_all_records(db:Session) -> list[RecordInfo]:
    return db.query(Record).all()

def get_my_records(token:str, db:Session):
    id: bytes = get_id(token)
    return db.query(Record).filter(Record.id_user == id)

def add_record(record: RecordAdd, token:str, db:Session) -> RecordInfo:
    record_db: Record = Record(**record.model_dump())

    #Verifico que el usuario tenga menos de 3 reservas para poder reservar.



    #Marco como False el campo available en book_unit.



    #Sumo +1 en el campo 'Rented_Books' del usuario.
    


    # Si todo esta bien: Añado a la bdd y retorno la info del libro agregado.
    # (Quizas deberia de agregar el id de la unidad y no de la obra.)
    db.add(record_db)
    db.commit()
    db.refresh(record_db)
    return record_db