from db.config import get_conexion
from fastapi import HTTPException
from models.product_model import Product
import aiomysql
import routes

# crear la funcion

async def get_products_list():
    try:
       # obtener acceso a la base de datos de forma asincrona 
       conn = await get_conexion()
       async with conn.cursor(aiomysql.DictCursor) as cursor:
        # consultamos datos
            await cursor.execute('SELECT * FROM upgrade_shop.products')
        # obtener los resultados
            data = await cursor.fetchall()
            conn.close()
            return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error mysql {str(e)}")





async def get_product_by_id(id_product):
    try: 
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM upgrade_shop.products WHERE id=%s', (id_product,))
            data = await cursor.fetchone()
        conn.close()
        if data:
            return data
        else:
            raise HTTPException(
                status_code=404, detail='producto no encontrado')
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f'error mysql {str(e)}')


