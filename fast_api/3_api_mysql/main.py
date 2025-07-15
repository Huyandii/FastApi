from fastapi import FastAPI
from routes import product_routes

# levantar el servidor y crear el acceso a la ruta product

app = FastAPI()
app.include_router(product_routes.router, 
                   prefix='/products', 
                   tags=['Products'])
