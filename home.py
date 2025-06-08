import streamlit as st
import time

st.set_page_config(page_title="Stick Cricket Showdown", page_icon="🏏", layout="wide")
st.subheader("Welcome to the ultimate cricket arcade")

theme = st.selectbox("Choose Theme", ["🌞 Light", "🌙 Dark"], index=0)

light_mode = theme == "🌞 Light"

st.markdown(f"""
<style>
html, body {{
background-color: {'#ffffff' if light_mode else '#0e1117'};
color: {'#000000' if light_mode else '#ffffff'};
}}
.main-container {{
background-color: {'#f9f9f9' if light_mode else '#1c1c1c'};
padding: 2rem;
border-radius: 20px;
margin-top: 1rem;
box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}}
h1 {{
font-size: 3rem;
text-align: center;
color: {'#e94e77' if light_mode else '#ff8080'};
text-shadow: 1px 1px 2px #444444;
}}
h3 {{
text-align: center;
font-weight: 400;
color: {'#333' if light_mode else '#ccc'};
}}
ul {{
font-size: 1.1rem;
}}
.footer {{
text-align: center;
font-size: 0.9rem;
color: gray;
margin-top: 2rem;
}}
</style>
""", unsafe_allow_html=True)

with st.container():
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("<h1>🏏 Stick Cricket Showdown</h1>", unsafe_allow_html=True)
st.markdown("<h3>Mini arcade-style cricket game built in Streamlit</h3>", unsafe_allow_html=True)

with st.spinner("Preparing your cricket kit..."):
    time.sleep(1)
st.success("You're ready to go!")

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    ### 🚀 How to Play:
    - 👤 Create your player profile
    - ⚙️ Set up match: overs, wickets, AI level
    - 🏏 Bat smart: choose shots, avoid outs
    - 🎯 Bowl tactically: aim for wickets
    - 📊 Check Scorecard for match results
    """)
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/en/f/f7/Stick_Cricket_Classic_Logo.png", width=220)

st.markdown("👉 Use the sidebar to move between game stages.")
st.balloons()

st.markdown("<div class='footer'>Made with ❤️ using Python & Streamlit | Rishi's Cricket Arcade</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
