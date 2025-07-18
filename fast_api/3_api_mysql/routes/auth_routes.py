from fastapi import APIRouter
from controllers import auth_controller
from models.user_model import UserCreate, UserLogin

router = APIRouter()

# creamos el registro de usuarios
@router.post('/register',status_code=201)
async def register(user: UserCreate):
    return await auth_controller.register(user)
# CREAMOS EL CONTROLLADOR
# IR A MAIN Y CREAR EL APP.INCLUDE_ROUTER


# -----
# Crear ruta de login de usuario:
@router.post('/login', status_code=200)
async def login(user_login: UserLogin):
    return await auth_controller.login(user_login)
# CREAR LA FUNCION LOGIN