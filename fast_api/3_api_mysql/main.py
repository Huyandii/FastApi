from fastapi import FastAPI
from routes import product_routes, user_routes, auth_routes

# levantar el servidor y crear el acceso a la ruta product

app = FastAPI()



app.include_router(product_routes.router, 
                   prefix='/products', 
                   tags=['Products'])



app.include_router(user_routes.router, 
                   prefix='/users', 
                   tags=['Users'])


# DE SECURITY
app.include_router(auth_routes.router, prefix='/auth', tags=['Auth'])
