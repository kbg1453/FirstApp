from sqlalchemy.orm import Session
from ..repositories import city_repository
from ..schemas.city_schema import CityCreate

# Geschäftslogik für City
def create_city(db: Session, city: CityCreate):
    db_city = city_repository.get_city_by_name(db, name=city.name)
    if db_city:
        return db_city
    return city_repository.create_city(db, city)

def get_all_cities(db: Session):
   return  city_repository.get_all_cities (db)
   