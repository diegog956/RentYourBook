from pydantic import BaseModel, Field, EmailStr
from uuid import UUID
from datetime import date
from app.api.utils.enums import Role


class UserRegister (BaseModel):
    '''
    Modelo para registro de usuario.
    '''
    # id_users: UUID = UUID() No lo ingresa el usuario.

    username: str 
    password: str = Field(min_length=8)
    verify_password: str
    name: str
    lastname: str
    email: EmailStr
    birthdate: date

    #Estos modelos no se colocan ya que no quiero que el usuario los ingrese. 
    #Los agrego en otro modelo y sqlalchemy eventualmente.

    # role: Role = Role.USER
    # warning_amount: int = 0
    # ban: bool = False