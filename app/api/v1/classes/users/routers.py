from fastapi import APIRouter, Depends, status, HTTPException
from pydantic import ValidationError
from .schemas import UserRegister, UserInfo
from uuid import UUID
import app.api.v1.classes.users.service as service
from sqlalchemy.orm import Session
from app.api.v1.database.database import get_db


user_router = APIRouter()


#<----------- GET ----------->#

'[GET] Retorna la Home que prueba el enrutamiento (?)'
@user_router.get('/', response_model=list[UserInfo],status_code=status.HTTP_200_OK)
async def home_user(db: Session = Depends(get_db)):
    return service.get_all_users(db)

'[GET] Devuelve la informacion del usuario por su id' #PROTEGER
@user_router.get('/{id}', response_model=UserInfo ,status_code=status.HTTP_200_OK)
async def get_one_user(id: UUID, db: Session = Depends(get_db)):
    return service.get_user_info(id, db)
   

'''Tener cuidado con rutas como '/all' ya que toma como que 'all' es un id! Ver ejemplo abajo.'''
# '[GET] Devuelve todos los usuarios para listado en seccion admin' #PROTEGER
# @user_router.get('/all', response_model=list[UserInfo], status_code=status.HTTP_200_OK)
# async def get_all_users(db:Session=Depends(get_db)):
#     return service.get_all_users(db)

#<----------- POST ----------->#

'[POST] Envia a la base de datos la informacion del usuario a crear' 
@user_router.post('/register', status_code=status.HTTP_201_CREATED, response_model= UserInfo) #PROTEGER
async def register(user_register: UserRegister, db: Session = Depends(get_db)):
    
    try:
        return service.register_user(user_register,db)
    
    except ValueError as e:
        #Es siempre raise http exception, no return!
        if 'password' in str(e):
            raise HTTPException(detail= str(e), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

    
    
