import os
from dotenv import load_dotenv

# Lädt Umgebungsvariablen aus einer .env-Datei
load_dotenv()

# Konfigurationseinstellungen für die Anwendung
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
CONNECTIONSTRING = os.getenv("CONNECTIONSTRING")
# PostgreSQL-Verbindungs-URL für SQLAlchemy
DATABASE_URL = f"postgresql://{SUPABASE_KEY}@{SUPABASE_URL}/postgres"
#DATABASE_URL =CONNECTIONSTRING