from fastapi import FastAPI, status
from app.api.v1.classes.users.routers import user_router
from app.api.v1.auth.authentication import login_router

app = FastAPI()


app.include_router(user_router, prefix='/api/v1/users', tags=['Users'])
app.include_router(login_router, prefix='/api/v1', tags=['Login'])

@app.get('/', status_code=status.HTTP_200_OK)
def home():
    return 'OK'

