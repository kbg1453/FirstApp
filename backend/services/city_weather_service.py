from sqlalchemy.orm import Session
from ..repositories import city_weather_repository
from ..schemas.city_weather_schema import CityWeatherCreate

# Geschäftslogik für CityWeather
def create_city_weather(db: Session, city_weather: CityWeatherCreate):
    return city_weather_repository.create_city_weather(db, city_weather)
