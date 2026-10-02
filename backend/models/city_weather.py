# models/city_weather.py
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class CityWeather(Base):
    __tablename__ = 'city_weather'

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    temperature = Column(Float)
    weather_description = Column(String)

    # Beziehung zu City
    city = relationship("City", back_populates="weather_data")
