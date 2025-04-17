
import streamlit as st

def predict_action(temp, rainfall, moisture):
    if temp > 30 and rainfall < 50 and moisture < 30:
        return "Irrigate"
    elif rainfall > 100:
        return "No irrigation needed"
    else:
        return "Monitor soil moisture"

st.set_page_config(page_title="GreenAlert", page_icon="🌿")
st.title("🌿 GreenAlert – Tea Garden Climate Assistant")
st.subheader("Smart AI Advice for Tea Farmers in Sreemangal")

st.markdown("Provide local data below to get instant suggestions:")

temp = st.number_input("🌡️ Temperature (°C)", min_value=0, max_value=50, value=28)
rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0, max_value=300, value=60)
moisture = st.number_input("💧 Soil Moisture (%)", min_value=0, max_value=100, value=35)

if st.button("🧠 Get AI Advice"):
    result = predict_action(temp, rainfall, moisture)
    st.success(f"✅ Climate Action Advice: **{result}**")
