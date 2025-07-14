from models.user_model import cargar_usuarios, usuario_por_id, guardar_usuario, modificar_usuario, buscar_email_nombre, buscar_por_edad
from models.user_model import User

def obtener_usuarios():
    return cargar_usuarios()


def usuario_por_did(id : int):
    return usuario_por_id(id)


def insertar_usuario(usuario: User):
    return guardar_usuario(usuario)


def borrar_usuario(id: int):
    return borrar_usuario(id)

# def actualizar_usuario(usuario: User )

def actualizar_usuario(id: int, usuario_actualizado: User):
    return modificar_usuario(id, usuario_actualizado)

# ----------------------------------

def filter_by_age(agemin: int, agemax: int):
    return buscar_por_edad(agemin, agemax)


def filterByText(busqueda: str):
    return buscar_email_nombre(busqueda)