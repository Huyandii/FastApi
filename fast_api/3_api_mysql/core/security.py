# Necesitamos las librerias de python llamadas python-jose => criptografia, passlib => bcrypt
# pip install  "python-jose[cryptografhy]" 
# pip install "passlib[bcrypt]"

import os #la nececitamos para cargar variables de entorno
from datetime import datetime, timedelta, timezone #se necesita para generarr la expiracion del token

from jose import JWTError, jwt #libreria de seguridad y encriptacion
from passlib.context import CryptContext# para hasear contraseñas
from dotenv import load_dotenv# para las variables de entorno



load_dotenv()   # cargar las variables de entorno

# leer las variables de entorno y almacenarlas para nuestro uso en este fichero:
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Configurar  bcrypt para poderlo usar en este fichero, para ello tengo que generar lo que es llamado contexto.
pwd_context = CryptContext(schemes='bcrypt', deprecated='auto')

 # encriptar contraseña
def hast_password(password: str):
    # hasea una contraseña usandp bcrypt
    return pwd_context.hash(password) 


def verify_password(plain_password: str, hashed_password: str):
    # Verifica que la contraseña en texto plano coincidaa con su hast.
    return pwd_context.verify(plain_password, hashed_password)

#TODO:VAMOS A RUTAS Y CREAMOS UN FICHERO LLAMADO auth.routes.py 


#  crear un token de logeo de usuario:
# un token se forma normalmente con el id_usuariio, rol, fecha de expiracion, {id: user.id,  rol: user.rol}

def create_token(data: dict): 
    # crear un token con la libreria JWT con los datos y expiracion
    datacopy_to_encode = data.copy()

    # ahora calculamos la fecha de expiracion usando la variable ACCESS_TOKEN en minutos:
    expire = datetime.now(tz=timezone.utc) + timedelta(minutes=ACCESS_TOKEN)

    # mi objetivo es crear un objeto que tenga {id: user.id,  rol: user.rol,  expire: tiempo}
    datacopy_to_encode.update({'expire': int(expire.timestamp())})
    # hasearlo (codificarlo)
    return jwt.encode(datacopy_to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    # lo decodigicamos para recibir los datoa de id, rol  del usuario logado, para ello usamos la libreria jwt
    try:
        #decode
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload 
    except JWTError:
        return None
# utilizar en el dependencies









# print(create_token({'id': 2, 'rol': 'admin' }))

