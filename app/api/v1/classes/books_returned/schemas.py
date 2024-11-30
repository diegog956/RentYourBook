from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from .models import BookReturned

class BookReturnedInfo(BaseModel):

    id_records:int
    id_user: UUID
    id_book_unit: int
    date_take: datetime
    return_date: datetime

    class config:
        orm_mode:True

    @classmethod
    def from_orm(cls, book_returned:BookReturned):
        return cls(id_user = UUID(bytes=book_returned.id_user))