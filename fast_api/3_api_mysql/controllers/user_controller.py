from db.config import get_conexion
from fastapi import HTTPException
from models.user_model import User 
import aiomysql
import routes



# --------------------------

async def get_one_user(id_user):
    try: 
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM upgrade_shop.users WHERE id=%s', (id_user,))
            data = await cursor.fetchone()
        
        if data:
            return data
        else:
            raise HTTPException(
                status_code=404, detail='Usuario no encontrado')
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f'error mysql {str(e)}')
    finally:
        conn.close()

#     id: int
    # name: str
    # surname: str
    # age: int
    # mail: EmailStr
    # register_date: Optional[datetime] = None
    # status: int
    # password: str
    # rol: str

# UPDATE USER
async def update_user(id_user: int, user: User):
      if id_user != user.id:
        raise HTTPException(status_code=400, detail='El usuario no coincide')
      try:
          conn = await get_conexion()
          async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('UPDATE upgrade_shop.users SET name=%s, surname=%s, age=%s, mail=%s, status=%s,password=%s, rol=%s WHERE id=%s', (
                user.name,
                user.surname,
                user.age,
                user.mail,
                user.status,
                user.password,
                user.rol,
                id_user
                ))
            await conn.commit()
            
            user = await get_one_user(id_user)
            return {'msg': 'Usuario actualizado', "item": user}
      except Exception as e:
          raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
      finally:
          conn.close()



