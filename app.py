
import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.title("AI Football Fixture Generator")

teams = st.text_area(
    "Enter team names, one per line",
    "Arsenal\nChelsea\nLiverpool\nManchester City"
).splitlines()

st.header("Tournament Fixtures")

for i in range(len(teams)):
    for j in range(i + 1, len(teams)):
        st.write(teams[i], "vs", teams[j])

st.header("AI Match Prediction")

data = pd.DataFrame({
    "Home": [2, 1, 3, 0, 2, 1],
    "Away": [0, 1, 1, 2, 1, 3],
    "Result": ["Win", "Draw", "Win", "Lose", "Win", "Lose"]
})

model = DecisionTreeClassifier()
model.fit(data[["Home", "Away"]], data["Result"])

home = st.number_input("Home team recent average goals", 0.0, 10.0, 2.0)
away = st.number_input("Away team recent average goals", 0.0, 10.0, 1.0)

if st.button("Predict Match"):
    prediction = model.predict([[home, away]])
    st.success("AI Prediction: " + prediction[0])
