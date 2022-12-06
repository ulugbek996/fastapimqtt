from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, BigInteger, MetaData , Table
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

metadata = MetaData()
class Region(Base):
    __tablename__ = "regions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Balans(Base):
    __tablename__ = "tashkilot"
    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"))
    name = Column(String, unique=True, index=True)

class District(Base):
    __tablename__ = "districts"
    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"))
    name = Column(String, unique=True, index=True)

class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Station(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True, index=True)
    id_nomer = Column(Integer, unique=True, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"))
    balans_id = Column(Integer, ForeignKey("tashkilot.id"))
    district_id = Column(Integer, ForeignKey("districts.id"))
    name = Column(String, unique=True, index=True)
    imei = Column(BigInteger, unique=True, index=True)
    lat = Column(Float)
    lon = Column(Float)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    telphone_sensor = Column(String)
    telphone_balans = Column(String)
    status = Column(Boolean, server_default=text('true'))
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, server_default=text('now()'))



class DataWaterHour(Base):
    __tablename__= 'data_water_hour'
    id = Column(Integer, primary_key=True, index=True)
    st_id = Column(Integer, ForeignKey("stations.id"))
    level = Column(Float)
    flow = Column(Float)
    time = Column(String)
    corection = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))



class DataWaterDay(Base):
    __tablename__= 'data_water_day'
    id = Column(Integer, primary_key=True, index=True)
    st_id = Column(Integer, ForeignKey("stations.id"))
    level = Column(Float)
    flow = Column(Float)
    time = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))



class DataWaterMonth(Base):
    __tablename__= 'data_water_month'
    id = Column(Integer, primary_key=True, index=True)
    st_id = Column(Integer, ForeignKey("stations.id"))
    level = Column(Float)
    flow = Column(Float)
    time = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class DataWellHour(Base):
    __tablename__= 'data_well_hour'
    id = Column(Integer, primary_key=True, index=True)
    st_id = Column(Integer, ForeignKey("stations.id"))
    level = Column(Float)
    meloration = Column(Float)
    time = Column(String)
    temprature = Column(Float)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class DataWellDay(Base):
    __tablename__= 'data_well_day'
    id = Column(Integer, primary_key=True, index=True)
    st_id = Column(Integer, ForeignKey("stations.id"))
    level = Column(Float)
    meloration = Column(Float)
    time = Column(String)
    temprature = Column(Float)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class DataWellMonth(Base):
    __tablename__= 'data_well_month'
    id = Column(Integer, primary_key=True, index=True)
    st_id = Column(Integer, ForeignKey("stations.id"))
    level = Column(Float)
    meloration = Column(Float)
    time = Column(String)
    temprature = Column(Float)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))










Name = Table(
    "names",
    metadata,
    Column( "id", Integer, primary_key=True, index=True),
    Column("name", String, unique=True, index=True),
)
DataReal1 = Table(
    "data_real",
    metadata,
    Column( "id", Integer, primary_key=True, index=True),
    Column("level", Float),
    Column("flow", Float),
    Column("imei", BigInteger),
    Column("time", String),
    Column("corection", Integer),
    Column("created_at", TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()')),
)

DataWaterHour1 = Table(
    "data_water_hour",
    metadata,
    Column( "id", Integer, primary_key=True, index=True),
    Column("st_id", Integer, ForeignKey("stations.id")),
    Column("level", Float),
    Column("flow", Float),
    Column("time", String),
    Column("corection", Integer),
    Column("created_at", TIMESTAMP(timezone=True),
                           nullable=False, server_default=text('now()')),
)

Station1 = Table(
    "stations",
    metadata,
    Column( "id", Integer, primary_key=True, index=True),
    Column("id_nomer", Integer, unique=True, index=True),
    Column("region_id", Integer, ForeignKey("regions.id")),
    Column("balans_id", Integer, ForeignKey("tashkilot.id")),
    Column("district_id", Integer, ForeignKey("districts.id")),
    Column("name", String, unique=True, index=True),
    Column("imei", BigInteger, unique=True, index=True),
    Column("lat", Float),
    Column("lon", Float),
    Column("sensor_id", Integer, ForeignKey("sensors.id")),
    Column("telphone_sensor", String),
    Column("telphone_balans", String),
    Column("status", Boolean, server_default=text('true')),
    Column("created_at", TIMESTAMP, server_default=text('now()')),
    Column("updated_at", TIMESTAMP, server_default=text('now()')),
)