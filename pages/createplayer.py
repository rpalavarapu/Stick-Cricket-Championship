import streamlit as st

st.title("👤 Create Your Player")

player_name = st.text_input("Enter your player name:")
batting_style = st.selectbox("Choose your batting style:", ["Aggressive", "Balanced", "Defensive"])
avatar = st.radio("Choose Avatar:", ["🏏", "🧔", "👩‍🦱", "🤖"])

if st.button("Save Player"):
    st.success(f"Player {player_name} saved! Let's go score some runs.")
    st.session_state["player_name"] = player_name
    st.session_state["style"] = batting_style
    st.session_state["avatar"] = avatar
