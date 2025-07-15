from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()


class Product (BaseModel):
    id: int
    title: str
    price: float
    quantity: int
    status: int


def get_conexion():
    return mysql.connector.connect(
        host="localhost",
        port=8889,
        user="root",
        password="root",
        database="upgrade_shop"
    )


@app.get('/products', status_code=200)
def get_products():
    # 1 - obtener acceso a la BBDD
    conn = get_conexion()
    # 2 - coloco el puntero a indice en ultimo disponible
    cursor = conn.cursor(dictionary=True)
    # 3 - consultar el pool de datos
    cursor.execute('SELECT * FROM upgrade_shop.products')
    # 4 - convertir el pool de datos en json
    data = cursor.fetchall()
    conn.close()
    return data
