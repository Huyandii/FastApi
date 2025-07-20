# ARCHIVOS DE DEPENDENCIASME PERMITEN BLOQUEAR EL ACCESO A CIERTAS RUTAS EN FUNCION DE CIERTTAS CARACTERISTICAS, SI EL USUARIO VALIDO O EL TIPO DE ROL QUE TIENE.

from fastapi import HTTPException, Depends, Path
from fastapi.security import OAuth2PasswordBearer
from db.config import get_conexion
from controllers. user_controller import get_one_user
import aiomysql
from core.security import decode_token
# A las sdeoendencias hay que indicarles donde y cuando se genera el toke
oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")



async def get_current_user(token : str = Depends(oauth2)):
    # decodificar el token
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail='token invalid')
    user_id = payload.get('id')
    if not user_id:
        raise HTTPException(status_code=405, detail='Este usuario no existe')
    # Obtener los datos del usuario lofado.
    user = await get_one_user(user_id)
    return user 

# Verificar si soy rol ADMIN o el propio usuario, esta dependencia nos servira para aplicar el crud de los usuarios
          # admin  or   user 
async def is_admin_or_owner(user=Depends(get_current_user), id_user:int = Path(...)):
    # verificar si el usuario autentificado es admin o es dueño del recurso. Si no se cumple esto: lanzo una excepcion
    # Si el usuario es admin, PERMITIR
    if user['rol']== 'admin':
        return user
    # Si el usuario es dueño del recurso
    if user['id'] == id_user:
        return user
    # si no se cumple nunguno, DENEGAR ACCESO
    raise HTTPException(status_code=403, detail='No tienes permisos para realizar esta accion')