from pydantic import BaseModel
from .city_schema import City

# Schema für CityWeather
class CityWeatherBase(BaseModel):
    temperature: int

class CityWeatherCreate(CityWeatherBase):
    city_id: int

class CityWeather(CityWeatherBase):
    id: int
    city: City

    class Config:
        orm_mode = True
