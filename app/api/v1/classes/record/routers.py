from fastapi import APIRouter, Depends,status
import app.api.v1.classes.record.service as service
from app.api.v1.database.database import get_db
from sqlalchemy.orm import Session
from app.api.v1.auth.authentication import oauth2_scheme
from .schemas import RecordInfo
from app.api.v1.auth.authentication import verify_admin_access


record_router = APIRouter()

@record_router.get('/all/', response_model=list[RecordInfo], status_code=status.HTTP_200_OK,dependencies=[Depends(verify_admin_access)])
async def get_all_records(db: Session = Depends(get_db)):
    '''Ruta exclusiva para el administrador'''
    return service.get_all_records(db)


@record_router.get('/', response_model=list[RecordInfo], status_code=status.HTTP_200_OK)
async def get_my_records(token:str = Depends(oauth2_scheme), db:Session = Depends(get_db)):
    return service.get_my_records(token, db)