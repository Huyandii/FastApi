from fastapi import APIRouter

from controllers import users_controller
from models.user_model import User






#en este fichero ya nos encontramos en la ruta /users, tdas la s rutas que creemos tendran esa base

router = APIRouter()
def get_users():
    return {'msg': 'devuelvo la ruta de usuarios'}

@router.get('/', status_code=200)#obtener todos los usuarios
def list_users():
    return users_controller.obtener_usuarios()



@router.get('/{id}', status_code=200)#obtener un usuarios por id
def get_byid_user(id: str):
    return users_controller.usuario_por_did(int(id))


# Endpoint POST
@router.post('/', status_code=201)  # Insertar un usuario
def post_user(usuario: User):
    return users_controller.guardar_usuario(usuario)



@router.delete('/{id}', status_code=200) #borrar usuario
def delete_user(id: str):
    return users_controller.borrar_usuario(int(id))




# actualizar usuario

@router.put('/{id}', status_code=200)  
def put_usuario(id: str, usuario_actualizado: User):
    return users_controller.actualizar_usuario(int(id), usuario_actualizado)
# ---------------------------------------------------




# Query params son parametros que no tienen una ruta fija = pero siempre recibe el mismo parametro. Me permiten hacer busquedas por marametros mas versatiles, se usan principalmente para filtros.



# rutas con filtros por edad http://localhost:8000/users/filter/age?agemin=12&agemax=24

@router.get('/filter/age', status_code=200) 
def get_user_by_age(agemin: int, agemax: int):
    return users_controller.filter_by_age(agemin, agemax)




#  http://localhost:8000/users/filter/search?busqueda=juanantonio
# @router.get('/filter/search', status_code=200) 
# def get_user_by_search(busqueda: str):
#     return users_controller.filterByText(busqueda)


# http://localhost:8000/users/filter/name?busqueda=

@router.get('/filter/name', status_code=200)
def filterByText(busqueda: str):
    return users_controller.filterByText(busqueda)

