from fastapi import FastAPI
from zaatot.routes import indexx
from fastapi_sqlalchemy import DBSessionMiddleware
from zaatot.db import SQLALCHEMY_DB_URL

app = FastAPI()

app.add_middleware(
    DBSessionMiddleware,
    db_url=SQLALCHEMY_DB_URL,
)
app.include_router(indexx.router)
