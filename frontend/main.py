import streamlit as st
import requests
from components.select_box_component import select_city, select_language
from config import LANGUAGES, API_URL, OPENWEATHERMAP_API_KEY, DISCORD_WEBHOOK_URL

st.title("City and Language Selector")

# Auswahl der Stadt über die API
response = requests.get(f"{API_URL}/cities/")
cities = response.json()
selected_city = select_city(cities)
st.write(f"Ausgewählte Stadt: {selected_city}")

# Auswahl der Sprache aus der Konfigurationsdatei
selected_language = select_language(LANGUAGES)
st.write(f"Ausgewählte Sprache: {selected_language}")

# Funktion zum Abrufen von Wetterdaten
def fetch_weather(city_name,language ):
    city_name ="Stuttgart"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{language}&appid={OPENWEATHERMAP_API_KEY}&units=metric&lang={language}"
    response = requests.get(url)
    return response.json()

# Funktion zum Senden einer Discord-Nachricht
def send_discord_message(content):
    data = {"content": content}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    return response.status_code

# Button zum Abrufen und Speichern der Wetterdaten
if st.button("Aktualisiere Wetterdaten"):
    weather_data = fetch_weather(selected_city,selected_language)
    st.write("Wetterdaten:", weather_data)

    # Extrahiere relevante Wetterinformationen
    weather_info = {
        "city_name": selected_city,
        "temperature": weather_data["main"]["temp"],
        "weather": weather_data["weather"][0]["description"]
    }

    # Speichere die Wetterdaten in Supabase
   # response = requests.post(f"{API_URL}/weather/", json=weather_info)
    #if response.status_code == 200:
        # Sende eine Nachricht an Discord
    discord_status = send_discord_message(f"Wetterdaten für {selected_city} wurden aktualisiert und gespeichert.")
    if discord_status == 204:
        st.success("Daten abgeholt, Datenbank gespeichert und Discord gemeldet!")
    else:
        st.error("Fehler beim Senden der Discord-Nachricht.")
   # else:
   #     st.error("Fehler beim Speichern der Wetterdaten.")