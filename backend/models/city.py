from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    country = Column(String)
    # Beziehung zu CityWeather
    weather_data = relationship("CityWeather", back_populates="city")