from sqlalchemy.orm import Session
from ..models.city_weather import CityWeather

def __init__(self, db: Session):
    self.db = db


def get_weather_by_city_id(db: Session, city_id: int):
    return db.query(CityWeather).filter(CityWeather.city_id == city_id).first()

def create_city_weather(db: Session, city_weather: CityWeather):
    db.add(city_weather)
    db.commit()
    db.refresh(city_weather)
    return city_weather