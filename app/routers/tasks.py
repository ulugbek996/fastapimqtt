from fastapi import FastAPI , APIRouter ,Depends
from fastapi_utils.tasks import repeat_every
from ..database import get_db , SessionLocal ,conn , engine , database
from .. import models, schemas
from .. worker import vaqt_uzgartirish
router = APIRouter(prefix="/tasks", tags=["tasks"])
@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()





@router.on_event("startup")
@repeat_every(seconds=60, raise_exceptions=True)
async def task():
    data = conn.fastapi.data.find()
    for i in data:
        try:
            query = models.Station1.select().where(models.Station1.c.imei == i["imei"])
            my_station = await database.fetch_one(query=query)
            if my_station:
                data_shcemas = schemas.DataCreate(**i)
                data_shcemas.st_id = my_station.id
                data_shcemas.time = vaqt_uzgartirish(data_shcemas.time)
                query = models.DataWaterHour1.insert().values(**data_shcemas.dict())
                last_record_id = await database.execute(query)
                print(last_record_id)
            conn.fastapi.data.delete_one({"_id": i["_id"]})
        except Exception as e:
            print(e)






