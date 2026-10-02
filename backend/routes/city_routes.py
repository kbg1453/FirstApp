from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.city_schema import City, CityCreate
from ..services.city_service import create_city, get_all_cities
from ..database import get_db

router = APIRouter()

# API-Routen für City
@router.post("/cities/", response_model=City)
def create_city_endpoint(city: CityCreate, db: Session = Depends(get_db)):
    return create_city(db, city)

@router.get("/cities/")
def get_all_cities_endpoint(city: CityCreate, db: Session = Depends(get_db)):
    return get_all_cities(db)