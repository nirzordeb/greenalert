
import streamlit as st
import requests

# ✅ Use your real API key here
API_KEY = "45a639fc080aea68034627c083e5b60b"

def predict_action(temp, rainfall, moisture):
    if temp > 30 and rainfall < 50 and moisture < 30:
        return "Irrigate"
    elif rainfall > 100:
        return "No irrigation needed"
    else:
        return "Monitor soil moisture"

def get_weather_data(city="Sreemangal"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        rainfall = data.get('rain', {}).get('1h', 0) or 0
        return temp, humidity, rainfall
    else:
        return None, None, None

st.set_page_config(page_title="GreenAlert", page_icon="🌿")
st.title("🌿 GreenAlert – Tea Garden Climate Assistant")
st.subheader("Real-Time AI Climate Advice for Sreemangal Farmers")

st.markdown("Provide or fetch local data below to get instant suggestions:")

# Input fields
temp = st.number_input("🌡️ Temperature (°C)", min_value=0, max_value=50, value=28, key="temp_input")
rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0, max_value=300, value=60, key="rain_input")
moisture = st.number_input("💧 Soil Moisture / Humidity (%)", min_value=0, max_value=100, value=35, key="moisture_input")

if st.button("🌐 Fetch Real-Time Weather (Sreemangal)"):
    temp, humidity, rainfall = get_weather_data()
    if temp is not None:
        st.session_state.temp_input = temp
        st.session_state.moisture_input = humidity
        st.session_state.rain_input = rainfall
        st.success(f"📍 Real Weather: Temp {temp}°C, Rainfall {rainfall}mm, Humidity {humidity}%")
    else:
        st.error("⚠️ Could not fetch weather data. Please check the API key or your internet connection.")

if st.button("🧠 Get AI Advice"):
    result = predict_action(temp, rainfall, moisture)
    st.success(f"✅ Climate Action Advice: **{result}**")
