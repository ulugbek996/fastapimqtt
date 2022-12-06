from pydantic import BaseModel, Field
from typing import  Optional


class DataInput(BaseModel):
    imei:int = Field(alias="i")
    time:str = Field(alias="t")
    level:float = Field(alias="d")
    flow:float = Field(alias="v")
    corection:int = Field(alias="c")

class DataReal(BaseModel):
    imei:int
    time:str
    level:float
    flow:float
    corection:int



class DataCreate(BaseModel):
    st_id: Optional[int]
    time:str
    level:float
    flow:float
    corection:int

class StationCreate(BaseModel):
    imei:str
    name:str
    lat:float
    lon:float
    region_id:int
    balans_id:int
    district_id:int
    sensor_id:int

class StationOut(BaseModel):
    _id:str
    imei:str
    name:str
    lat:float
    lon:float
    region_id:int
    balans_id:int
    district_id:int
    sensor_id:int

class NameInput(BaseModel):
    name: str


class NameOut(BaseModel):
    id: int
    name: str


class Info(BaseModel):
    imei: str = Field(alias="i")
    time: str = Field(alias="t")
    region_id: str = Field(alias="p1")
    balans_id: str = Field(alias="p2")
    name: str = Field(alias="p3")
    tel_seria: str = Field(alias="p4")
    tel_number: str = Field(alias="p5")
    locatsiya: str = Field(alias="p6")
    tempratura: str = Field(alias="p7")
    batery: str = Field(alias="p8")
    signal: str = Field(alias="p9")
    proshivka: str = Field(alias="p10")
    frivers: str = Field(alias="p11")
    time1: str = Field(alias="p12")
    time2: str = Field(alias="p13")
    time3: str = Field(alias="p14")
    time4: str = Field(alias="p15")
    sensor_id: str = Field(alias="p16")
    sensor_name:Optional[str] = Field(alias="p17")

class Alert1(BaseModel):
    imei:int = Field(alias="i")
    time:str = Field(alias="t")
    region_id:int = Field(alias="p1")
    balans_id:int = Field(alias="p2")
    name:str = Field(alias="p3")
    tel_seria:str = Field(alias="p4")
    tel_number:str = Field(alias="p5")
    batery:int = Field(alias="p6")
    status:str = Field(alias="p7")


class Alert2(BaseModel):
    imei:int = Field(alias="i")
    time:str = Field(alias="t")
    region_id:int = Field(alias="p1")
    balans_id:int = Field(alias="p2")
    name:str = Field(alias="p3")
    tel_seria:str = Field(alias="p4")
    tel_number:str = Field(alias="p5")
    lokatsiya:str = Field(alias="p6")
    status:str = Field(alias="p7")