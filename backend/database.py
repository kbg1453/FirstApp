from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL

# Datenbankverbindung
#engine = create_engine(DATABASE_URL)
try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"An error occurred: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Base.metadata.create_all(bind=engine)

# Abhängigkeitsfunktion für die Datenbank-Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
