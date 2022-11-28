from pydantic import BaseModel, Field
from typing import  Optional



class DataInput(BaseModel):
    imei:int = Field(alias="i")
    time:str = Field(alias="t")
    level:float = Field(alias="d")
    flow:float = Field(alias="v")
    corection:int = Field(alias="c")

