from fastapi import APIRouter, status, Depends
from app.api.v1.auth.authentication import verify_admin_access, get_db
from .schemas import BookReturnedInfo
from sqlalchemy.orm import Session
from uuid import UUID
from . import service 

bookreturned_router = APIRouter()

@bookreturned_router.get('/all/{amount}', response_model=list[BookReturnedInfo], status_code=status.HTTP_200_OK, dependencies=[Depends(verify_admin_access)])
async def get_all_old_records(amount : int, db: Session = Depends(get_db)):
    return service.get_all_old_records(amount, db)

@bookreturned_router.get('/{id}', response_model=list[BookReturnedInfo], status_code=status.HTTP_200_OK)
async def get_old_recods_by_id(id: UUID, db: Session = Depends(get_db)):
    return service.get_old_records_by_id(id, db)