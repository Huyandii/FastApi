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



# PRECIO MAYOR Y MENOR
async def get_by_price(min_price, max_price):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM upgrade_shop.products WHERE price BETWEEN %s AND %s', (min_price, max_price))
            data = await cursor.fetchall()
        conn.close()
        if data:
            return data
        else: 
            raise HTTPException(
                status_code=404, detail='Producto no encontrado')
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f'error mysql {str(e)}')
    


    # NOMBRE TITLE

async def get_by_title(title):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            query = 'SELECT * FROM upgrade_shop.products WHERE LOWER(title) LIKE %s'
            value = f"%{title.lower()}%"
            await cursor.execute(query, (value,))
            data = await cursor.fetchall()
        conn.close()

        if data:
            return data
        else:
            raise HTTPException(
                status_code=404, detail='Nombre del producto no encontrado')

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error mysql {str(e)}')





# STOCK = 0

async def get_by_zero_stock():
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM upgrade_shop.products WHERE status = 0')
            data = await cursor.fetchall()
        conn.close()

        if data:
            return data
        else:
            return HTTPException(status_code=404, detail='No se encontraron productos fuera de stock')
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error mysql {str(e)}')
    





    #   STOCK +10


async def get_by_medio_stock():
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM upgrade_shop.products WHERE quantity > 10')
            data = await cursor.fetchall()
        conn.close()

        if data:
            return data
        else:
            return HTTPException(status_code=404, detail='no se han encontrado los productos')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error mysql {str(e)}')