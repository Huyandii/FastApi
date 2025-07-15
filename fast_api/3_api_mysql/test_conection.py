from fastapi import FastAPI 
from pydantic import BaseModel
from dotenv import load_dotenv
import aiomysql
import os
app = FastAPI()
load_dotenv()

# creacion del modelo en base a nuestra base de datos
# la funcion get_conexion tiene que ser asincrona
async def get_conexion():
    return await aiomysql.connect(
        host=os.getenv('MYSQL_HOST'),
        port=int(os.getenv('MYSQL_PORT')),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        db=os.getenv('MYSQL_DATABASE')
    )


class Product(BaseModel):
    id: int
    title: str
    price: float
    quantity: int
    status: int


# Usando el fichero .env, utilizando la libreria dotenv de python




@app.get('/')
def init():
    return 'Conexion iniciada con el servidor'


@app.get('/products', status_code=200)
async def get_all_products():
    # optener el acceso a la base de datosm asincrona
    conn = await get_conexion()
    # situo el cursor  al final de mi tabla para consultar todos los datos de la misma
    async with conn.cursor(aiomysql.DictCursor) as cursor:
        # Consultar los datos 
        await cursor.execute('SELECT * FROM upgrade_shop.products')
        # obtener os resultados
        data = await cursor.fetchall()
    conn.close()
    return data

