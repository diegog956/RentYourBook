from .models import Record
from sqlalchemy.orm import Session
from .schemas import RecordInfo
from app.api.v1.auth.authentication import get_id

def get_all_records(db:Session) -> list[RecordInfo]:
    return db.query(Record).all()

def get_my_records(token:str, db:Session):
    id: bytes = get_id(token)
    return db.query(Record).filter(Record.id_user == id)

