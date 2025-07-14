from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Quiero generar una ruta por GET para que me devuelva una respuesta.

# Voy a generar un enpoint estatico

# utilizamos algo llamado decorador = una funcion  que convierte 
@app.get('/ee') #http://localhost:8000/ee
def root():
    return {'mensaje':
            'Hola mundo desde FastAPI'}
# Crear una ruta "/mi_nombre" que me devuelve un objeto alumno con vuestro nombre 

@app.get ('/mi_nombre')
def get_name():
    return{'alumno': 'Juan Antonio'}


products = [
    {'id': 1, 'name': 'leche', 'price': 2 },
    {'id': 2, 'name': 'carne', 'price': 23 },
    {'id': 3, 'name': 'Huevos', 'price': 6 },
    {'id': 4, 'name': 'Lechuga', 'price': 7 },
    {'id': 5, 'name': 'Pan', 'price': 62 },
    {'id': 6, 'name': 'Pescado', 'price': 82 },
]


@app.get('/productos')
def get_products():
    return {'total': len(products), 'results': products}



# endpoint dinamico
@app.get('/productos/{id}')
def get_productos_by_id(id: str):
    id_producto = int(id)
    for product in products:
        if product['id'] == id_producto:
            return product
        else:
            return {'mesage': f'No existe el producto con el id {id_producto}'} 
          
# Quiero un endpoint que me permita filtrar productos por precio por minimo y maximo


@app.get('/precios/{price_min}/{price_max}')
def get_productos_by_price(price_min: str, price_max: str):
    result = []
    for product in products:
        if product['price'] >= float(price_min) and product['price'] <= float(price_max):
            result.append(product)
    if len(result) !=0:
        return result
    else:
        return 'No hay productos con ese precio'
    
# insercion de un producto creando un modelo Product. utilizaremos una libreria de python que se llama Pydantic
class Product(BaseModel):
    id: int
    name: str
    price: float
    
@app.post('/productos')
def crear_producto(producto: Product):
    #insertar el producto en el array
    products.append(producto)
    # return {'mgs': f'Producto {producto.name} registrado correctmaente'}
    return (products)

#borrar un producto del array de producto
@app.delete('/productos/{id}')
def borrar_producto(id: str):

    for product in products:
        if product['id'] == int(id):
            products.remove(product)
            return{'mgs': 'producto borrado', 'results': products}
    return{'msg': 'producto no existe'}