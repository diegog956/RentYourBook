from fastapi import APIRouter


record_router = APIRouter()


record_router.get('/')
async def get_all_records():
    return 'OK'

@record_router.get('/{id}')
async def get_records_from_one_user(id:int):
    '''Retorna los registros de un usuario por su id'''
    return 'OK'
