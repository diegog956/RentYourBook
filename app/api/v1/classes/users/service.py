from app.api.v1.classes.users.schemas import UserRegister
from app.api.v1.database.database import get_db
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .models import User
from uuid import uuid4
from app.api.v1.utils.enums import Role
import bcrypt

def register_user(user: UserRegister, db: Session):

    #Faltaria buscar si no existe ya un email registrado!

    hashed_password = bcrypt.hashpw(user.hashed_password.encode('utf-8') , bcrypt.gensalt())
    user.hashed_password = hashed_password
    
    new_user: User = User(
    hashed_password = user.hashed_password, 
    name = user.name,
    lastname =user.lastname,
    email = user.email,
    birthdate = user.birthdate,
     id_user= uuid4().bytes
    , rented_books=0
    , user_role=Role.user)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return user

