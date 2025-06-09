import streamlit as st

st.set_page_config(page_title="Scorecard")
st.title("📊 Match Scorecard")

required_keys = ["match_ready", "your_team", "opponent", "overs", "batting_first", "innings"]
if not all(k in st.session_state for k in required_keys):
    st.error("⚠ Please play the match first by completing the Match Setup and Live Match.")
    st.stop()

team1 = st.session_state["batting_first"]
team2 = st.session_state["opponent"] if team1 == st.session_state["your_team"] else st.session_state["your_team"]

team1_runs = st.session_state.get("team1_runs", 0)
team1_balls = st.session_state.get("team1_balls", 0)
team1_out = st.session_state.get("team1_out", False)

team2_runs = st.session_state.get("team2_runs", 0)
team2_balls = st.session_state.get("team2_balls", 0)
team2_out = st.session_state.get("team2_out", False)

def display_score(team, runs, balls, out):
    overs = f"{balls // 6}.{balls % 6}"
    st.markdown(f"### 🏏 {team}")
    st.markdown(f"*Score:* {runs}/{1 if out else 0}")
    st.markdown(f"*Overs:* {overs}")
    st.markdown("---")

display_score(team1, team1_runs, team1_balls, team1_out)

if st.session_state["innings"] == 2 or team2_balls > 0 or team2_out:
    display_score(team2, team2_runs, team2_balls, team2_out)

    if team2_balls >= st.session_state["overs"] * 6 or team2_out:
        st.markdown("## 🏁 Match Result")

        if team1_runs > team2_runs:
            st.success(f"🎉 {team1} won by {team1_runs - team2_runs} runs!")
        elif team2_runs > team1_runs:
            st.success(f"🔥 {team2} won by {10 - (1 if team2_out else 0)} wickets!")
        else:
            st.info("🤝 It's a Tie!")

else:
    st.info("🔄 Second innings in progress... Play the rest in *Live Match*.")