from fastapi import APIRouter, status
from .schemas import UserRegister
user_router = APIRouter()

@user_router.get('/', status_code=status.HTTP_200_OK)
def home_user():
    return 'USERS.'


@user_router.post('/register', status_code=status.HTTP_201_CREATED)
def register(user_register: UserRegister):
    return user_register.__dict__