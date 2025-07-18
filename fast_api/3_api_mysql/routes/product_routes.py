from fastapi import APIRouter, Depends
from controllers import product_controller 
from models.product_model import Product, ProductCreate
from core.dependencies import get_current_user


router = APIRouter()




# http://localhost:8000/products/
@router.get('/', status_code=200)
async def get_all(user=Depends(get_current_user)):
    return await product_controller.get_products_list()# PASAR DEPENDENCIA 


@router.get('/id/{id_product}', status_code=200)
async def get_product_id(id_product: int):
    return await product_controller.get_product_by_id(id_product)



#TODO: practicar una ruta que me permita sacar uno o varios productos por un precio minimo y maximo 

@router.get('/price/{min_price}/{max_price}', status_code=200)

async def get_price(min_price: float , max_price: float):
    return await product_controller.get_by_price(min_price, max_price)






#TODO: quiero una ruta que me permita sacar un producto por su titulo, debera devolverme una lista de productos. SI ESCRIBE IPHONE => todos los que incluyan la palabra iphone en en el titulo

@router.get('/title/{title}', status_code=200)

async def get_title(title: str):
    return await product_controller.get_by_title(title)





#TODO: Quiero una ruta que me permita devolver un listado de productos que no esten en el stock.

@router.get('/stock/0', status_code=200)

async def get_zero_stock():
    return await product_controller.get_by_zero_stock()







#TODO: Quiero una ruta que me permita devolever un listado de productos con cantidad(stock) mayor a 10

@router.get('/stock/hibrido', status_code=200)

async def get_medio_stock():
    return await product_controller.get_by_medio_stock()



#TODO: Borrar productos. DEL y para no borrar toda la base de datos debemos borrar por ID 

@router.delete('/delete/{id_product}', status_code=200)
async def delete_product(id_product: int):
    return await product_controller.delete_product(id_product)




# TODO: Crear un producto . POST mandaremos la informacion del producto que queremos registrar, ojo sin ID. 
# la respuesta debera devolverme los datos completos del producto creado con id
@router.post('/', status_code=201)
async def create_product(product: ProductCreate):
    return await product_controller.create_product(product)



# TODO: Actualizacion  de un prodfucto: PUT/PAT. actualizamos la informacion de la base de datos, ojo aqui si tenemos id. La respuesta debera ser como minimo el producto actualizado

@router.put('/{id_product}', status_code=200)
async def update_product(id_product: int, product: Product):
    return await product_controller.update_product(id_product, product)