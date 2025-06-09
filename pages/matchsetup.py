import streamlit as st

st.title("🗓️ Match Setup")

teams = ["India", "Australia", "England", "South Africa", "New Zealand"]
your_team = st.selectbox("Select Your Team", teams)
opponent = st.selectbox("Select Opponent", [team for team in teams if team != your_team])
overs = st.slider("Select number of overs", 1, 10, 5)
pitch = st.radio("Pitch Type", ["Flat", "Green", "Dusty"])

if st.button("Confirm Match"):
    st.session_state["match_ready"] = True
    st.session_state["your_team"] = your_team
    st.session_state["opponent"] = opponent
    st.session_state["overs"] = overs
    st.session_state["pitch"] = pitch
    st.success("Match setup saved! Head to Live Match!")