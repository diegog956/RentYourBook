from fastapi import FastAPI, status
from app.api import user_router

app = FastAPI()





@app.get('/', status_code=status.HTTP_200_OK)
def home():
    return 'OK'

