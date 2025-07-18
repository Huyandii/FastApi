# from fastapi import HTTPException, Depends, Path                #Middleware
# from fastapi.security import OAuth2PasswordBearer
# from db.config import get_conexion
# from controllers.user_controller import get_one_user
# from core.security import decode_token
# import aiomysql

# async def get_current_user(token: str):
#     payload = decode_token(token)
#     if not  payload:
#         raise HTTPException(status_code=401, detail='token invalido')
    
#     user_id = payload.get('id')
#     if not user_id:
#         raise HTTPException(status_code=404, detail='usuario no existe')
#     user = await get_one_user(user_id)#<---   obtener los datos del usuario logado:
#     return user
# #  LE AÑADIMOS UNA RUTA A PRODUCT ROUTES
# ----------------------------------------------------------------------------------se borro




# ARCHIVOS DE DEPENDENCIASME PERMITEN BLOQUEAR EL ACCESO A CIERTAS RUTAS EN FUNCION DE CIERTTAS CARACTERISTICAS, SI EL USUARIO VALIDO O EL TIPO DE ROL QUE TIENE.

from fastapi import HTTPException, Depends, Path
from fastapi.security import OAuth2AuthorizationCodeBearer
from db.config import get_conexion
from controllers. user_controller import get_one_user
import aiomysql