from app.api.v1.classes.users.schemas import UserRegister, UserInfo,UserChangeProfileData
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

def unban(id: UUID,db:Session) -> str:
    user: User = db.query(User).filter(User.id_user == id.bytes).first()
    if user:
        user.ban = False
        db.add(user)
        db.commit()
        db.refresh(user)
        return f'User id: {id} was successfully unbaned.'
    else:
        raise ValueError('User not found')

def modify(id: UUID, user: UserChangeProfileData, db:Session) -> str:
    sql_user: User = db.query(User).filter(User.id_user == id.bytes).first()
    
    if sql_user is None:
        raise ValueError('User not found.')
    elif bcrypt.checkpw(user.password.encode('utf-8'),sql_user.hashed_password.encode('utf-8')) is False:
        raise ValueError('Wrong password. Unauthorize access.')
    else:
        sql_user.name = user.name 
        sql_user.lastname = user.lastname
        sql_user.email = user.email
        sql_user.birthdate = user.birthdate
        db.add(sql_user)
        db.commit()
        db.refresh(sql_user)
        return sql_user
