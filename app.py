import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="DRIVE - Live Emergency System",
    page_icon="🚑",
    layout="centered"
)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align:center; color:red;'>🚑 DRIVE Emergency System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;'>Live GPS Location Sharing System</h4>",
    unsafe_allow_html=True
)

st.divider()

st.write("📍 Click the button below to fetch your REAL-TIME location")

# ---------------- LIVE GPS COMPONENT ----------------
components.html("""
<div style="text-align:center;">
    <button onclick="getLocation()" 
        style="padding:12px 20px; font-size:16px; border-radius:10px; cursor:pointer;">
        📍 Get Live Location
    </button>

    <p id="status" style="margin-top:15px;"></p>
</div>

<script>
function getLocation() {
    const status = document.getElementById("status");
    status.innerHTML = "Fetching location... ⏳";

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

# ---------------- INFO ----------------
st.info("⚠️ Allow location permission when browser asks for it")
st.success("🚑 This system can be used for emergency location sharing")
