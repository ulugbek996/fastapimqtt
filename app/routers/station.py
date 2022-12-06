from fastapi import FastAPI , APIRouter ,Depends
from ..database import get_db , SessionLocal ,conn
from .. import models, schemas
from typing import List
router = APIRouter(prefix="/station", tags=["station"])


@router.get("/", response_model=List[schemas.StationOut])
async def find_get_stations():
    data = conn.fastapi.station.find()
    return [schemas.StationOut(**i) for i in data]




@router.get("/{id}")
async def find_get_station(id: str):
    data = conn.fastapi.station.find_one({"_id": id})
    return data


@router.post("/")
async def create_station(station: schemas.StationCreate):
    conn.fastapi.station.insert_one(station.dict())
    return station
