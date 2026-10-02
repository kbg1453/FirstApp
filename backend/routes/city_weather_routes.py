from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.city_weather_schema import CityWeather, CityWeatherCreate
from ..services.city_weather_service import create_city_weather
from ..database import get_db

router = APIRouter()

# API-Routen für CityWeather
@router.post("/city_weather/", response_model=CityWeather)
def create_city_weather_endpoint(city_weather: CityWeatherCreate, db: Session = Depends(get_db)):
    return create_city_weather(db, city_weather)
