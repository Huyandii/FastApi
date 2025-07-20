from fastapi import APIRouter
from controllers import villager_controller
from models.villager_model import Villager


route = APIRouter()

# LISTA DE ALDEANOS
@route.get('/', status_code=200)
async def villagers_list():
    return await villager_controller.villagers_list()

# VER ALDEANO POR ID
@route.get('/{id_villager}', status_code=200)
async def get_villager(id_villager: int):
    return await villager_controller.get_one_villager(id_villager)


# ACTUALIZAR ALDEANO POR ID
@route.put('/{id_villager}', status_code=200)
async def update_villager(id_villager: int, villager: Villager):
    return await villager_controller.update_villager(id_villager, villager)


# BORRAR ALDEANO POR ID
@route.delete('/{id_villager}', status_code=200)
async def delete_villager(id_villager: int):
    return await villager_controller.delete_villager(id_villager)


