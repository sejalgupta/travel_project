from sqlalchemy import create_engine, Column, Integer, String, REAL
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()
TABLE_NAME = "cityAttractions"

#Set up table with Attractions object
class Attraction(Base):
    __tablename__= TABLE_NAME
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    attraction = Column(String())
    attraction_information = Column(String())
    latitude = Column(REAL())
    longitude = Column(REAL())
    location = Column(String())

    def __init__(self, attraction, attraction_information, latitude, longitude, location):
        self.attraction = attraction
        self.attraction_information = attraction_information
        self.latitude = latitude
        self.longitude = longitude
        self.location = location

    def __repr__(self):
        return "Attraction %s: %s" % (int(self.id), self.attraction)