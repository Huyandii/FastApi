from pydantic import BaseModel


class Product(BaseModel):
    id: int
    title: str
    price: float
    quantity: int
    status: int


# Para poder pasarle un producto sin id 
class ProductCreate(BaseModel):
    title: str
    price: float
    quantity: int
    status: int



# --------------------------

