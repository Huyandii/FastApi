from pydantic import BaseModel
from datetime import date


# ID ALDEANO
class Villager(BaseModel):
    id : int
    name: str
    species: str
    rol: bool
    personality: str
    birthday: date
    hobby: str
    fruta: str


#   "name": "Canela",
#   "species": "Perro",
#   "rol": 1,
#    "personality": "Tímido",
#   "birthday": "2025-10-16",
#   "hobby": "Deporte",
#   "fruta": "Cereza"
# }