from pydantic import BaseModel
from fastapi import HTTPException


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

usuarios = [
    {"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 30, "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "age": 22, "email": "charlie@example.com"},
    {"id": 4, "name": "Diana", "age": 28, "email": "diana@example.com"},
    {"id": 5, "name": "Eve", "age": 35, "email": "eve@example.com"},
    {"id": 6, "name": "Frank", "age": 40, "email": "frank@example.com"},
    {"id": 7, "name": "Grace", "age": 27, "email": "grace@example.com"},
    {"id": 8, "name": "Hank", "age": 32, "email": "hank@example.com"},
    {"id": 9, "name": "Ivy", "age": 29, "email": "ivy@example.com"},
    {"id": 10, "name": "Jack", "age": 24, "email": "jack@example.com"}
]
def cargar_usuarios():
    return usuarios



# def usuario_por_id(id: int):
#     for usuario in usuarios:
#         if usuario['id'] == id:
#             return True
#     return {'msg': f'usuario {id} no encontrado'}

def usuario_por_id(id: int):
    for usuario in usuarios:
        if usuario['id'] == id:
            return usuario  # Antes devolvías True, lo corregimos
        raise HTTPException(status_code=404, detail='Usuario no encontrado') 






# Buscar por email
def buscar_usuario_email(email: str):
    for usuario in usuarios:
        if usuario['email'] == email:
            return True
    return False







# Guardar nuevo usuario
def guardar_usuario(usuario: User):
    if not buscar_usuario_email(usuario.email):
        usuarios.append(usuario.model_dump())  # Convertimos el objeto User a dict ---- ahora se usa el model_dump()-> es una funcion que convierte a un usuario en un tipo user en un diccionario para hacer append en un array
        return usuarios
    else:
        raise HTTPException(status_code=404, detail='Usuario duplicado')


# quiero que implementeis en 5 minutos el borrado del un usuario del array, debereis devolver la lista de usuarios sin el usuario que quiero borrar.


# def borrar_usuario_id(id: int):
#     usuario_borrar = usuario_por_id(id)
#     if usuario_borrar:
#         usuarios.remove(usuario_borrar)
#         return usuarios
#     else:
#         return {'msg': 'no existe'}








def borrar_usuario(id: int):
    usuario_borrar = usuario_por_id(id)
    

    if usuario_borrar and usuario_borrar['id']:
        usuarios.remove(usuario_borrar)
        return {'msg': f'Usuario con id {id} borrado correctamente', 'usuarios': usuarios}
    
    else:
        raise HTTPException(status_code=400, detail='Usuario no encontrado')
        return {'msg': 'Usuario no existe'}





# def actualizar_usuario(id: int):
#     put_usuario = usuario_por_id(id)

#     if put_usuario['id']:
#         usuarios.update(usuario_por_id)
#         return {'msg': f'usuario {id} actualizado'} and cargar_usuarios
#     else:
#         return {'msg': 'No se ha encontrado el usuario'}

    



def modificar_usuario(id: int, usuario_actualizado: User):
    for index, usuario in enumerate(usuarios):
        if usuario['id'] == id:
            usuarios[index] = usuario_actualizado.model_dump()
            return {'msg': f'Usuario con id {id} actualizado correctamente', 'usuario': usuarios[index]}
        
    raise HTTPException(status_code=404, detail='usuario no encontrado')



# ------------------------------------ 10:00



def buscar_por_edad(agemin: int, agemax: int):
    if agemin > agemax :
        raise HTTPException(
            status_code=400, detail='La edad minima no puedad ser mayor que la maxima') 
    
    usuarios_busqueda = []
    for user in usuarios:
        if user['age'] >= agemin and user['age'] <= agemax:
            usuarios_busqueda.append(user)
    return usuarios_busqueda
        






#Teneis que decirme si existe un nombre o email que contenga lo que tiene busqueda. Juan => Juan, Juan Antonio, Juan jose, juan@gmail.com, manueljuan@gmail.com. Me tendria que devolver todos los datos del alumno => array.




def buscar_email_nombre(busqueda: str):
    if busqueda == "":
        raise HTTPException(
            status_code=400, detail='El campo de busqueda no puede ser vacio')
    return (usuario for usuario in usuarios if busqueda.lower() in usuario['name'].lower() or busqueda.lower() in usuario['email'].lower())




    # usuario_buscado = []

    # for usuario in usuarios:
    #     if usuario['name'] == busqueda or usuario['email'] == busqueda:
    #         usuario_buscado.append(usuario)

    # if len (usuario_buscado) == 0:
    #     raise HTTPException(status_code=404, detail='Usuario no encontrado')
    
    # return usuario_buscado



