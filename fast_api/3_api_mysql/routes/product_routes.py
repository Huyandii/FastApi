from fastapi import APIRouter
from controllers import product_controller
from models import product_model

router = APIRouter()


# http://localhost:8000/products/
@router.get('/', status_code=200)
async def get_all():
    return await product_controller.get_products_list()


@router.get('/{id_product}', status_code=200)
async def get_product_id(id_product: int):
    return await product_controller.get_product_by_id(id_product)

#TODO: practicar una ruta que me permita sacar uno o varios productos por un precio minimo y maximo 

#TODO: quiero una ruta que me permita sacar un producto por su titulo, debera devolverme una lista de productos. SI ESCRIBE IPHONE => todos los que incluyan la palabra iphone en en el titulo

#TODO: Quiero una ruta que me permita devolver un listado de productos que no esten en el stock.

#TODO: Quiero una ruta que me permita devolever un listado de productos con cantidad(stock) mayor a 100