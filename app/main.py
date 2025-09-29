from fastapi import FastAPI
from app.routers import items

app = FastAPI(title="Catálogo de Celulares")

app.include_router(items.router)

