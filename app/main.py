from fastapi import FastAPI
from .database import engine
from . import models
from  .routers  import  mqtt

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(mqtt.router)