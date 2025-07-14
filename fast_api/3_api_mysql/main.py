from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

class Products(BaseModel):
    id: int
    title: str
    price: float
    quantity: int
    status: int


def get_conexion():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "anghel",
        database = "upgrade_shop_"
    )

@app.get('/products', status_code=200)
def get_products():
    # 1 - obtener acceso a la BBDD
    conn = get_conexion()
    # 2 - coloco el puntero  o indice y lo coloco en el ultimo disponible
    cursor = conn.cursor()
    # 3 - consultar el pool de datos
    cursor.execute('SELECT * FROM upgrade_shop_.products')
    # 4 - convertir el pool en json 
    data = cursor.fetchall()
    conn.close()
    return data

