from fastapi import FastAPI , APIRouter ,Depends
from fastapi_mqtt import FastMQTT, MQTTConfig
from .. import models, schemas
from sqlalchemy.orm import Session
import json
import psycopg2
from ..database import get_db , SessionLocal ,conn
router = APIRouter(prefix="/mqtt", tags=["mqtt"])

mqtt_config = MQTTConfig(host= '185.196.214.190',
                         port= 1883,
                         username= "emqx",
                         password= "12345",
                         keepalive = 60)

mqtt = FastMQTT(
    config=mqtt_config
)

mqtt.init_app(router)



@mqtt.on_connect()
def connect(client, flags, rc, properties):
    mqtt.client.subscribe("/mqtt") #subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)

#@mqtt.on_message()
#async def message(client, topic, payload, qos, properties):
#   print("Received message: ",topic, payload.decode(), qos, properties)

@mqtt.subscribe("W/+/+/+/data")
async def message_to_topic( client, topic, payload, qos, properties ):
    try:
        data_shcemas = schemas.DataInput(**json.loads(payload.decode()))
        conn.fastapi.data.insert_one(data_shcemas.dict())
    except Exception as e:
      pass

@mqtt.subscribe("W/+/+/+/info")
async def message_to_topic( client, topic, payload, qos, properties ):
    try:
        data_shcemas = schemas.Info(**json.loads(payload.decode()))
        conn.fastapi.info.insert_one(data_shcemas.dict())
    except Exception as e:
      print(e)

@mqtt.subscribe("W/+/+/+/alert1")
async def message_to_topic( client, topic, payload, qos, properties ):
    try:
        data_shcemas = schemas.Alert1(**json.loads(payload.decode()))
        conn.fastapi.alert1.insert_one(data_shcemas.dict())
    except Exception as e:
      pass


@mqtt.subscribe("W/+/+/+/alert2")
async def message_to_topic( client, topic, payload, qos, properties ):
    try:
        data_shcemas = schemas.Alert2(**json.loads(payload.decode()))
        conn.fastapi.alert2.insert_one(data_shcemas.dict())
    except Exception as e:
      pass



@mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

@mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)