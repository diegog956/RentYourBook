import pytest
from sqlalchemy.orm import sessionmaker
from app.api.database.database import get_db
from sqlalchemy.orm import Session

def test_get_db_type():
    #FastAPI lo hacia solo pero en testing se debe hacer manual.

    #Esto devuelve un generador:
    gen = get_db()

    #Pido el siguiente valor del yield:
    db = next(gen)

    #Corroboro si es de la misma clase que Session (Conexion temporal a la base de datos)
    assert isinstance(db, Session)

    #Cierro el generador para que llame al finally de get_db()
    gen.close()