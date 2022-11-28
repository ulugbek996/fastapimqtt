from fastapi import FastAPI , APIRouter ,Depends
from fastapi_mqtt import FastMQTT, MQTTConfig
from .. import models, schemas
from sqlalchemy.orm import Session
import json
import psycopg2
from ..database import get_db , SessionLocal ,conn
router = APIRouter(prefix="/mqtt", tags=["mqtt"])


#conn = psycopg2.connect("dbname=fastapi user=postgres password=12345 host=localhost")

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
    #print(conn.fastapi.data.find()
    data = conn.fastapi.data.find()
    for i in data:
        print(i)
    #db = SessionLocal()
    #cur = conn.cursor()
    #print(cur)
    #try:
  #      data_shcemas = schemas.DataInput(**json.loads(payload.decode()))
  #      conn.fastapi.data.insert_one(data_shcemas.dict())
  #  except Exception as e:
 #     print(e)

    #db.add(data_shcemas)
    #print(type(data_shcemas))
    #data = models.DataReal(**data_shcemas.dict())
    #print(data)


    #cur.execute("INSERT INTO data_real (level, flow, imei, time, corection) VALUES (%s, %s, %s, %s, %s)", (data.level, data.flow, data.imei, data.time, data.corection))
    #curs = conn.cursor()
    #conn.commit()
    #print(data)
    #db.add(data)
    #db.commit()
    #db.refresh(data)
    #print("Received message to specific topic: ", topic, payload.decode(), qos, properties)

@mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

#@mqtt.on_subscribe()
#def subscribe(client, mid, qos, properties):
#    print("subscribed", client, mid, qos, properties)