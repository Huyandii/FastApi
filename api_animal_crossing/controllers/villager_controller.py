from db.config import get_conexion
from fastapi import HTTPException
from models.villager_model import Villager
import aiomysql



# COGER UN ALDEANO
async def get_one_villager(id_villager):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM animal_crossing.villagers WHERE id=%s', (id_villager,))
            data = await cursor.fetchone()
        if data:
            return data
        else:
            raise HTTPException(status_code=404, detail=f'El aldeano con el id {id_villager} no esta en la base de datos')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error {str(e)}')
    finally:
        conn.close()




# LISTA DE ALDEANOS
async def villagers_list():
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM animal_crossing.villagers")

            data = await cursor.fetchall()
            return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error{str(e)}')
    finally:
        conn.close()




    # id : int
    # name: str
    # species: str
    # rol: bool
    # birthday: date
    # hobby: str
    # fruta: str
# ACTUALIZAR ALDEANO
async def update_villager(id_villager: int, villager: Villager):
    if id_villager != villager.id:
        raise HTTPException(status_code=400, detail='ID del aldeano no coincide')
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('UPDATE animal_crossing.villagers SET name=%s, species=%s, rol=%s, personality=%s, birthday=%s, hobby=%s, fruta=%s WHERE id=%s', (
                villager.name,
                villager.species,
                villager.rol,
                villager.personality,
                villager.birthday,
                villager.hobby,
                villager.fruta,
                id_villager
                ))
            await conn.commit()
            user = await get_one_villager(id_villager)
            return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()


# ELIMINAR ALDEANO
async def delete_villager(id_villager: int):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            user = await get_one_villager(id_villager)
            if not user:
                raise HTTPException(
                    status_code=404, detail='El aldeano no es residente')
           
            await cursor.execute('DELETE FROM animal_crossing.villagers WHERE id=%s', (id_villager,))
            await conn.commit()
            return {"msg": f"El aldeano {id_villager} se fue de la isla", "status": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()
