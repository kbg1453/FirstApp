from sqlalchemy.orm import Session
from ..models.city import City

def get_all_cities(self):
    # Logik, um alle Städte aus der Datenbank abzurufen
    return self.db.query(City).all()

# CRUD-Operationen für das City-Modell
def get_city_by_name(db: Session, name: str):
    return db.query(City).filter(City.name == name).first()

def create_city(db: Session, city: City):
    db.add(city)
    db.commit()
    db.refresh(city)
    return city