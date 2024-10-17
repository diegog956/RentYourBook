from pydantic import BaseModel, Field, EmailStr, model_validator, field_validator
from uuid import UUID
from datetime import date
from app.api.v1.utils.enums import Role
from typing_extensions import Self


class UserRegister (BaseModel):
    '''
    Modelo para registro de usuario.
    El usuario es el email.
    '''
    # id_users: UUID = UUID() No, ya que no lo ingresa el usuario.

    hashed_password: str 
    verify_password: str
    name: str
    lastname: str
    email: EmailStr
    birthdate: date

    #Estos modelos no se colocan ya que no quiero que el usuario los ingrese. 
    #Los agrego en otro modelo y sqlalchemy eventualmente.

    # verified_email: bool = False
    # role: Role = Role.USER
    # warning_amount: int = 0
    # ban: bool = False
    # rented_boooks = 0

    @model_validator(mode='after')
    def verify_passwords(self)-> Self:
        if self.hashed_password == self.verify_password:
            return self 
        else:
            raise ValueError('Passwords do not match')

    @field_validator('hashed_password')
    def check_password_length(cls, v):
        if len(v) < 8:
            raise ValueError("El password debe tener al menos 8 caracteres.")
        return v

class UserInfo(BaseModel):
    '''
    
    Modelo que asemeja a ORM y es devuelto al frontend
    para que el usuario visualice sus datos en perfil.
    
    '''

    # id_users: UUID No lo retorno por que es con el que lo busco.
    
    name: str
    lastname: str
    email: EmailStr
    birthdate: date
    role: Role
    #Agregar cuando cree entidad libros:
    #rented_books : List[Books]
    warning_amount: int
    ban: bool

class UserChangeProfileData(BaseModel):
    '''
    
    Establece el modelo para el cambio de datos
    en el perfil de usuario.
    (Los datos cambiables, como por ejemplo, dia de nacimiento.)
    
    Pensar en cambio de contraseña.

    '''
    
    name: str
    lastname: str
    email: EmailStr
    birthdate: date

 



