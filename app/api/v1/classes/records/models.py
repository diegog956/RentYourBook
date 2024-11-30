from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey
from sqlalchemy.dialects.mysql import BINARY as MySQLBinary
from sqlalchemy.orm import declarative_base
from app.api.v1.classes.users.models import User

Base = declarative_base()

class Record(Base):
    __tablename__ = 'Records'

    #En este caso on_delete = 'cascade' esta bien colocado, ya que si se elimina un usuario o un libro, quiero eliminar sus registros.

    id_records = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    id_user = Column(MySQLBinary, ForeignKey('Users.id_user', ondelete='cascade'), nullable=False)
    id_book_unit = Column(Integer, ForeignKey('Books.id_book', ondelete='cascade'), nullable=False)
    date_take = Column(DATETIME)
    expected_return_date = Column(DATETIME, nullable=False)

