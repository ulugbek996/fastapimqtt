from fastapi import FastAPI
from .database import engine
from . import models
from  .routers  import  mqtt , tasks , station

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(mqtt.router)
app.include_router(tasks.router)
app.include_router(station.router)