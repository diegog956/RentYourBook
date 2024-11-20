from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from dotenv import load_dotenv
import os
from app.api.v1.database.database import get_db
from sqlalchemy.orm import Session
from app.api.v1.classes.users.service import user_exists
from uuid import UUID
import datetime
from pydantic import BaseModel

'Este schema relaciona la autorizacion (boton authorize en swagger con la ruta post /login)'
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/login')

load_dotenv()

login_router = APIRouter()

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

@login_router.post('/login', response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    '''
    Recibo el formulario.
    Busco el usuario en la bdd.
    Si existe retorno un token para que acceda a las rutas que el desee.
    '''
    try:
        id: UUID = user_exists(form_data.username, form_data.password, db)
    except ValueError as e:
        raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
        
    payload={'id':str(UUID(bytes=id)),
                 'iat':datetime.datetime.now(datetime.timezone.utc)(),
                 'exp':(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)).timestamp(),
                 'scope': 'user'
                 }
    token: str = encode_token(payload=payload)
    return TokenResponse(access_token=token, token_type='Bearer')
    


def encode_token(payload: dict)-> str:
    'Recibe la informacion del usuario como diccionario y la retorna como token(str)'
    token: str = jwt.encode(payload, key=os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
    return token

def decode_token(token: str)-> dict:
    'Recibe el token y retorna la informacion del usuario.'
    payload: dict = jwt.decode(token=token, key=os.getenv('SECRET_KEY'), algorithms=os.getenv('ALGORITHM'))
    return payload

def verify_token():
    pass

def get_id(token: str) -> UUID:
    '''
    Crear funcion que tenga en su encabezado 
    el schema de oauth y retorne el id 'escondido'
    '''
    payload: dict = decode_token(token)
    
    return UUID(payload['id'])