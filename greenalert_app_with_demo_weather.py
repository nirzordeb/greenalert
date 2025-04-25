
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


import streamlit as st
import requests

# === SETTINGS ===
API_KEY = "45a639fc080aea68034627c083e5b60b"
LAT = 24.3083   # Sreemangal latitude
LON = 91.7296   # Sreemangal longitude

# === STYLING ===
st.set_page_config(page_title="GreenAlert 🌿", layout="centered")

st.markdown("""
    <style>
    .main {
        background-image: url('https://i.ibb.co/DkgM1w5/green-bg.jpg');
        background-size: cover;
        padding: 2rem;
        border-radius: 10px;
        color: white;
    }
    h1 {
        color: #ffffff;
        text-align: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# === UI START ===
st.title("🌿 GreenAlert")
st.subheader("Smart Weather Insights for Farmers of Sreemangal")

st.markdown("---")

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"].title(),
            "rain": data.get("rain", {}).get("1h", 0),
            "wind": data["wind"]["speed"]
        }
    else:
        return None

# === FETCH AND SHOW ===
if st.button("📡 Get Live Weather"):
    weather = get_weather()
    if weather:
        st.success("✅ Data fetched successfully!")
        st.metric("🌡️ Temperature", f"{weather['temp']} °C")
        st.metric("💧 Humidity", f"{weather['humidity']} %")
        st.metric("☁️ Condition", weather['weather'])
        st.metric("🌬️ Wind Speed", f"{weather['wind']} m/s")
        st.metric("🌧️ Rainfall (1h)", f"{weather['rain']} mm")

        # Sample AI-like logic
        if weather['rain'] > 5:
            st.warning("⚠️ Heavy rainfall detected. Avoid irrigation today.")
        elif weather['temp'] > 35:
            st.info("🌞 It's hot outside. Consider shading young crops.")
        else:
            st.success("🌱 Conditions are ideal for most crops.")
    else:
        st.error("⚠️ Could not fetch weather data. Check your API key or connection.")

st.markdown("---")
st.caption("🚀 Powered by Streamlit + OpenWeatherMap | Built with ❤️ by Nirzor & Rudroneel")

