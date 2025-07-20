from fastapi import APIRouter, Depends
from controllers import user_controller 
from models.user_model import User, UserCreate
from core.dependencies import is_admin_or_owner

router = APIRouter()



# LISTA DE USUARIOS
@router.get('/', status_code=200)
async def list_users():
    return await user_controller.list_users()


# USUARIO POR ID
@router.get('/get/{id_user}', status_code=200)
async def get_by_user(id_user: int):
    return await user_controller.get_one_user(id_user)


# ACTUALIZAR USUARIO POR ID
@router.put('/put/{id_user}', status_code=200)
async def update_user(id_user: int, user: User):
    return await user_controller.update_user(id_user, user)


#  BORRAR USUARIO POR ID
@router.delete('/{id_user}', status_code=200)                     #user
async def delete_user(id_user: int, admin_user=Depends(is_admin_or_owner)):
    return await  user_controller.delete_user(id_user)


# CREAR UN USUARIO
@router.post('/', status_code=200)
async def create_user(new_user: UserCreate):
    return await user_controller.create_user(new_user)