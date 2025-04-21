import streamlit as st
import requests

API_KEY = "45a639fc080aea68034627c083e5b60b"

def predict_action(temp, rainfall, moisture):
    if temp > 30 and rainfall < 50 and moisture < 30:
        return "💧 **Irrigate Now!**"
    elif rainfall > 100:
        return "🌧️ **No Irrigation Needed**"
    else:
        return "🌱 **Monitor Soil Moisture**"

def get_weather_data(lat=24.3083, lon=91.7296):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        rainfall = data.get('rain', {}).get('1h', 0) or 0
        return temp, humidity, rainfall
    else:
        st.error(f"⚠️ API Error {response.status_code}: {response.text}")
        return None, None, None

# Set up page layout and background with GitHub image link
st.set_page_config(page_title="GreenAlert", page_icon="🌿", layout="wide")
st.markdown("""
    <style>
        .reportview-container {
            background-image: url("https://github.com/nirzordeb/greenalert/blob/main/green_bg.jpg");
            background-size: cover;
            background-position: center;
            padding: 20px;
        }
        .title {
            text-align: center;
            color: white;
            font-size: 36px;
            font-family: 'Arial', sans-serif;
        }
        .subheader {
            text-align: center;
            color: white;
            font-size: 24px;
            font-family: 'Arial', sans-serif;
        }
        .button {
            background-color: #28a745;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 5px;
        }
        .button:hover {
            background-color: #218838;
        }
        .input-box {
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌿 GreenAlert – Tea Garden Climate Assistant")
st.subheader("Real-Time AI Climate Advice for Sreemangal Farmers")

# Input Fields with Style
temp = st.number_input("🌡️ Temperature (°C)", min_value=0, max_value=50, value=28, key="temp_input", step=0.1, format="%.1f")
rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0, max_value=300, value=60, key="rain_input", step=0.1, format="%.1f")
moisture = st.number_input("💧 Soil Moisture / Humidity (%)", min_value=0, max_value=100, value=35, key="moisture_input", step=1)

# Button for fetching real-time weather
if st.button("🌐 Fetch Real-Time Weather (Sreemangal)", key="fetch_weather", help="Get weather info based on your location"):
    temp, humidity, rainfall = get_weather_data()
    if temp is not None:
        st.session_state.temp_input = temp
        st.session_state.moisture_input = humidity
        st.session_state.rain_input = rainfall
        st.success(f"📍 Sreemangal Weather: Temp {temp}°C, Rainfall {
