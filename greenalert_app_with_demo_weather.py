
import streamlit as st
import random

def predict_action(temp, rainfall, moisture):
    if temp > 30 and rainfall < 50 and moisture < 30:
        return "Irrigate"
    elif rainfall > 100:
        return "No irrigation needed"
    else:
        return "Monitor soil moisture"

def get_demo_weather():
    # Demo values mimicking real-time weather data from Sreemangal
    return {
        "temperature": random.choice([27, 29, 31]),
        "rainfall": random.choice([45, 60, 120]),
        "moisture": random.choice([25, 35, 50])
    }

st.set_page_config(page_title="GreenAlert", page_icon="🌿")
st.title("🌿 GreenAlert – Tea Garden Climate Assistant")
st.subheader("Smart AI Advice for Tea Farmers in Sreemangal")

st.markdown("Provide local data below to get instant suggestions:")

# Inputs with default values
temp = st.number_input("🌡️ Temperature (°C)", min_value=0, max_value=50, value=28, key="temp_input")
rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0, max_value=300, value=60, key="rain_input")
moisture = st.number_input("💧 Soil Moisture (%)", min_value=0, max_value=100, value=35, key="moisture_input")

if st.button("🌐 Fetch Real-Time Weather (Demo)"):
    weather = get_demo_weather()
    st.session_state.temp_input = weather["temperature"]
    st.session_state.rain_input = weather["rainfall"]
    st.session_state.moisture_input = weather["moisture"]
    st.info(f"📍 Demo Weather from Sreemangal: Temp {weather['temperature']}°C, Rainfall {weather['rainfall']}mm, Moisture {weather['moisture']}%")

if st.button("🧠 Get AI Advice"):
    result = predict_action(temp, rainfall, moisture)
    st.success(f"✅ Climate Action Advice: **{result}**")
