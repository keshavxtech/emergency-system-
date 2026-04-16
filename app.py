import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(
    page_title="DRIVE Emergency System",
    page_icon="🚑",
    layout="centered"
)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align:center; color:red;'>🚑 DRIVE Emergency System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;'>Smart Accident Detection + Live Location Sharing</h4>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- SESSION ----------------
if "accident" not in st.session_state:
    st.session_state.accident = False

# ---------------- BUTTON ----------------
if st.button("🚨 Start Monitoring System"):
    st.info("System monitoring user activity...")

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    st.session_state.accident = True

# ---------------- ACCIDENT TRIGGER ----------------
if st.session_state.accident:
    st.error("🚨 ACCIDENT DETECTED!")

    st.warning("📍 Fetching Live GPS Location...")

    # ---------------- LIVE GPS ----------------
    components.html("""
    <div style="text-align:center;">
        <button onclick="getLocation()" 
            style="padding:12px 20px; font-size:16px; border-radius:10px;">
            📍 Share Live Location
        </button>

        <p id="status" style="margin-top:15px;"></p>
    </div>

    <script>
    function getLocation() {
        const status = document.getElementById("status");
        status.innerHTML = "Getting live location... ⏳";

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
            status.innerHTML = "Geolocation not supported ❌";
        }
    }

    function showPosition(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        document.getElementById("status").innerHTML =
            "📍 Latitude: " + lat + "<br>" +
            "📍 Longitude: " + lon + "<br><br>" +
            "<a target='_blank' href='https://www.google.com/maps?q=" 
            + lat + "," + lon + "'>🗺 Open in Google Maps</a>";
    }

    function showError() {
        document.getElementById("status").innerHTML = "Permission denied ❌";
    }
    </script>
    """, height=300)

    st.success("🚑 Emergency services notified (simulation)")
    st.info("👨‍👩‍👧 Location will be shared with emergency contacts")
