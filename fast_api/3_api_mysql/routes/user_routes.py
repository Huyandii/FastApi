from fastapi import APIRouter
from controllers import user_controller 
from models.user_model import User, UserCreate

router = APIRouter()



# LISTA DE USUARIOS
@router.get('/get/{id_user}', status_code=200)
async def get_by_user(id_user: int):
    return await user_controller.get_one_user(id_user)


@router.put('/put/{id_user}', status_code=200)
async def update_user(id_user: int, user: User):
    return await user_controller.update_user(id_user, user)