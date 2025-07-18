from core.security import hast_password, verify_password, create_token #IMPORTACION DE LA CARPETA CORE
from models.user_model import UserCreate, UserLogin
from controllers.user_controller import get_one_user
from db.config import get_conexion
from fastapi import HTTPException
import aiomysql
 

#  REGISTRAR USUARIO:
async def register(user: UserCreate):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            hashed_password = hast_password(user.password) # hasear el password

            # insertamos usuario:
            await cursor.execute('INSERT INTO upgrade_shop.users (name, surname, age, mail, password, rol) VALUES (%s, %s, %s, %s, %s, %s)', (
                user.name,
                user.surname,
                user.age,
                user.mail,
                hashed_password,
                user.rol
            ))

            await conn.commit()
            new_id =  cursor.lastrowid
            user = await get_one_user(new_id) #hay que importarlo de la carpeta controller
            return {'smg': 'Usuario registrado correctamente', 'item': user}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error {str(e)}')
    finally:
        conn.close()


# CREAR LA FUNCION LOGIN
async def login(user_login: UserLogin):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM upgrade_shop.users WHERE mail=%s', (user_login.mail,))
            user = await cursor.fetchone()

            if not user:
                raise HTTPException(status_code=404, detail='Usuario o password incorrecto')   #verificar contraseña
            if not verify_password(user_login.password, user['password']):#<--( Al ser un diccionario)
                raise HTTPException(status_code=404, detail='Usuario o password incorrecto')
            
            # CREAR EL TOKEN  
            token_data = { 'id': user['id'], 'rol': user['rol'] }
            token = create_token(token_data)
            return {
                'token': token,
                'type': 'bearer',
                'usuario': {
                    'id': user['id'],
                    'name': user['name'],
                    'rol': user['rol'],
                    'mail': user['mail']
                }
            }
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()