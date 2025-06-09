import streamlit as st
import random
import json
from streamlit_lottie import st_lottie

def load_lottie_file(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return None

st.set_page_config(page_title="Live Match")
st.title("🎮 Live Match")

required_keys = ["match_ready", "your_team", "opponent", "overs", "batting_first"]
if not all(k in st.session_state for k in required_keys):
    st.error("⚠ Match setup incomplete. Please go to the Match Setup page first.")
    st.stop()

six_url = "shots_animations/6.json"
four_url = "shots_animations/4.json"
wicket_url = "shots_animations/wicket.json"

batting_first = st.session_state["batting_first"]
bowling_first = st.session_state["opponent"] if batting_first == st.session_state["your_team"] else st.session_state["your_team"]

if "innings" not in st.session_state:
    st.session_state["innings"] = 1
    st.session_state["team1_runs"] = 0
    st.session_state["team1_balls"] = 0
    st.session_state["team1_out"] = False
    st.session_state["team2_runs"] = 0
    st.session_state["team2_balls"] = 0
    st.session_state["team2_out"] = False

innings = st.session_state["innings"]
batting_team = batting_first if innings == 1 else bowling_first
current_team = "team1" if innings == 1 else "team2"

runs = st.session_state[f"{current_team}_runs"]
balls = st.session_state[f"{current_team}_balls"]
out = st.session_state[f"{current_team}_out"]
max_balls = st.session_state["overs"] * 6

st.subheader(f"🏏 Inning {innings}: {batting_team} Batting")
st.markdown(f"🎯 Score: *{runs}/{1 if out else 0}*  |  🧮 Balls: *{balls}/{max_balls}*")

if not out and balls < max_balls:
    shot = st.selectbox("Choose your shot", ["Straight Drive", "Pull", "Cut", "Scoop", "Defend"], key=f"shot_{innings}")
    if st.button("Play Shot"):
        outcome = random.choices(
            ["Dot", "1", "2", "4", "6", "Wicket"],
            weights=[10, 15, 10, 20, 15, 5], k=1
        )[0]

        if outcome == "Wicket":
            st.error("You're OUT! 🏏")
            st.session_state[f"{current_team}_out"] = True
            anim = load_lottie_file(wicket_url)
            if anim: st_lottie(anim, speed=1, width=400, height=400, key=f"wicket_{innings}")
        else:
            st.success(f"You played a {shot} and scored: {outcome}")
            if outcome == "4":
                anim = load_lottie_file(four_url)
                if anim: st_lottie(anim, speed=1, width=400, height=400, key=f"four_{innings}")
            elif outcome == "6":
                anim = load_lottie_file(six_url)
                if anim: st_lottie(anim, speed=1, width=400, height=400, key=f"six_{innings}")

            st.session_state[f"{current_team}_runs"] += int(outcome) if outcome.isdigit() else 0
            st.session_state[f"{current_team}_balls"] += 1
else:
    if innings == 1:
        st.info("🛑 First Innings Over! Click to start the second innings.")
        if st.button("Start Second Innings"):
            st.session_state["innings"] = 2
    else:
        st.success("🏁 Match Over! You can now head to the Scorecard page.")

with st.expander("🌦 Match Conditions"):
    st.markdown(f"""
    - 🏟 *Stadium*: {st.session_state["stadium"]}
    - 🌤 *Weather*: {st.session_state["weather"]}
    - 🧱 *Pitch Type*: {st.session_state["pitch"]}
    - 🎯 *Bowling Style*: {st.session_state["bowling_type"]}
    """)