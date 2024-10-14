from fastapi import FastAPI, status
from app.api.v1.classes.users.routers import user_router

app = FastAPI()


app.include_router(user_router, prefix='/api/v1/users', tags=['Users'])


@app.get('/', status_code=status.HTTP_200_OK)
def home():
    return 'OK'

