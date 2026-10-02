from pydantic import BaseModel

# Schema für City
class CityBase(BaseModel):
    name: str
    country:str

class CityCreate(CityBase):
    pass

class City(CityBase):
    id: int

    class Config:
        orm_mode = True
