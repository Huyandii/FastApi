from fastapi import FastAPI
from routes import villager_route

app = FastAPI()

app.include_router(villager_route.route,
                   prefix='/villagers',
                   tags=['Villagers'])
