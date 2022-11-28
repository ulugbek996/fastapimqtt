from  sqlalchemy   import Column, Integer, String, Boolean, ForeignKey, Float
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class DataReal(Base):
    __tablename__= 'data_real'
    id = Column(Integer, primary_key=True, index=True)
    level = Column(Float)
    flow = Column(Float)
    imei = Column(Integer)
    time = Column(String)
    corection = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))