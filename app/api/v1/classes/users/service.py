from app.api.v1.classes.users.schemas import UserRegister, UserInfo
from app.api.v1.database.database import get_db
from app.api.v1.classes.users.models import User
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .models import User
from uuid import uuid4, UUID
from app.api.v1.utils.enums import Role
import bcrypt

def register_user(user: UserRegister, db: Session):

    sql_user: User = db.query(User).filter(User.email == user.email).first()
    if sql_user:
        raise ValueError('User already registered.')
    
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8') , bcrypt.gensalt())
    user.password = hashed_password
    
    new_user: User = User(
    hashed_password = user.password, 
    name = user.name,
    lastname =user.lastname,
    email = user.email,
    birthdate = user.birthdate,
     id_user= uuid4().bytes,
     warning_amounts = 0
    , rented_books=0
    , user_role=Role.user.value)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_info(id: UUID,db:Session) -> User:
    user: User = db.query(User).filter(User.id_user == id.bytes).first()
    if user is None:
        raise ValueError('User not found.')
    return user

def get_all_users(db:Session)-> list[User]:
    lista: list[User] = db.query(User).all()
    return lista

