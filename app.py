import streamlit as st
import time
import requests
import webbrowser

# -----------------------------
# PAGE CONFIG (TITLE + ICON)
# -----------------------------
st.set_page_config(
    page_title="DRIVE - Emergency System",
    page_icon="🚑",
    layout="centered"
)

# -----------------------------
# HEADER (Website Name)
# -----------------------------
st.markdown("<h1 style='text-align: center; color: red;'>🚑 DRIVE Emergency System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Smart Accident Detection & Location Sharing</h4>", unsafe_allow_html=True)

st.divider()

# -----------------------------
# LOCATION FUNCTION
# -----------------------------
def get_location():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()

        loc = data.get("loc", "28.7041,77.1025")
        lat, lon = loc.split(",")

        return {
            "lat": lat,
            "lon": lon,
            "city": data.get("city", "Unknown")
        }
    except:
        return {
            "lat": "28.7041",
            "lon": "77.1025",
            "city": "Delhi"
        }

# -----------------------------
# SESSION STATE
# -----------------------------
if "alert" not in st.session_state:
    st.session_state.alert = False

# -----------------------------
# MAIN BUTTON
# -----------------------------
if st.button("🚨 Start Emergency Monitoring"):
    st.info("System is monitoring user activity...")

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.session_state.alert = True

# -----------------------------
# EMERGENCY TRIGGER
# -----------------------------
if st.session_state.alert:
    st.error("🚨 ACCIDENT DETECTED!")

    location = get_location()

    st.success(f"📍 City: {location['city']}")
    st.write(f"Latitude: {location['lat']}")
    st.write(f"Longitude: {location['lon']}")

    maps_url = f"https://www.google.com/maps?q={location['lat']},{location['lon']}"

    st.markdown("### 🗺 Location Link")
    st.markdown(f"[Open in Google Maps]({maps_url})")

    if st.button("🚑 Dispatch Ambulance & Open Map"):
        webbrowser.open_new_tab(maps_url)

        st.warning("🚑 Ambulance dispatched...")
        time.sleep(2)

        st.info("📡 Ambulance on the way...")
        time.sleep(2)

        st.success("🏥 Patient picked up successfully!")
