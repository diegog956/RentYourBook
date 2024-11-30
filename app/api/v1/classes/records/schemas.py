from pydantic import BaseModel
from uuid import UUID
from app.api.v1.classes.records.models import Record
from datetime import datetime

class RecordAdd(BaseModel):
    id_user: UUID
    id_book_unit: int 
    date_take: datetime
    expected_return_date: datetime

class RecordInfo(BaseModel):

    id_records: int
    id_user: UUID
    id_book_unit: int 
    date_take: datetime
    expected_return_date: datetime

    @classmethod
    def from_orm(cls, record:Record):
        return cls(id_user = UUID(bytes=record.id_user))