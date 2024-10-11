from fastapi import FastAPI, status
from app.api.classes.users.routers import user_router

app = FastAPI()


app.include_router(user_router, prefix='/api/users', tags=['Users'])


@app.get('/', status_code=status.HTTP_200_OK)
def home():
    return 'OK'

