
st.header("AI Match Prediction")

home = st.number_input("Home team average goals", 0.0, 10.0, 2.0)
away = st.number_input("Away team average goals", 0.0, 10.0, 2.0)

if st.button("Predict Match"):
    if home > away:
        st.success("Prediction: Home Team Wins")
    elif away > home:
        st.success("Prediction: Away Team Wins")
    else:
        st.info("Prediction: Draw")

