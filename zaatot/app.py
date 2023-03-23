from fastapi import FastAPI
from zaatot.routes import indexx

app = FastAPI()

app.include_router(indexx.router)
