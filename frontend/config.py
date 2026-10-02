import os
from dotenv import load_dotenv


# Lädt Umgebungsvariablen aus einer .env-Datei
load_dotenv()

# Konfigurationseinstellungen für die Anwendung
LANGUAGES = os.getenv("LANGUAGES")
API_URL = os.getenv("API_URL")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")