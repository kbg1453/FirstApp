import streamlit as st
import requests

st.title("City Page")

# Hinzufügen einer neuen Stadt
st.header("Add a New City")
city_name = st.text_input("City Name")
country_name = st.text_input("Country Name")

if st.button("Add City"):
    if city_name and country_name:
        # Sende eine POST-Anfrage an den FastAPI-Endpoint
        response = requests.post(
            "http://localhost:8000/cities/",
            json={"name": city_name, "country": country_name}
        )
        
        if response.status_code == 200:
            st.success(f"City {city_name} added successfully!")
        else:
            st.error("Failed to add city. Please try again.")
    else:
        st.error("Please enter both city and country names.")
