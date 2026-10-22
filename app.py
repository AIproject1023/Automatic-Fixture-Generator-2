
import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.title("⚽ AI Football Fixture Generator")

data = pd.read_csv("results.csv")
X = data[["home_points", "away_points"]]
y = data["result"]

model = DecisionTreeClassifier(max_depth=3)
model.fit(X, y)

teams = st.text_area(
    "Enter Team,Points (one per line)",
    "Brazil,10\nFrance,8\nGermany,5\nArgentina,3"
)

if st.button("Generate Fixtures"):
    try:
        team_list = []
        for line in teams.splitlines():
            name, points = line.rsplit(",", 1)
            team_list.append((name.strip(), int(points)))

        if len(team_list) < 2:
            st.error("Enter at least 2 teams.")
        elif len({t[0].lower() for t in team_list}) != len(team_list):
            st.error("Team names must be unique.")
        elif any(p < 0 for _, p in team_list):
            st.error("Points cannot be negative.")
        else:
            team_list.sort(key=lambda t: t[1], reverse=True)

            st.subheader("Team Ranking")
            for i, (name, points) in enumerate(team_list, 1):
                st.write(f"{i}. {name} - {points} points")

            names = [t[0] for t in team_list]
            points = dict(team_list)

            if len(names) % 2:
                names.append("BYE")

            st.subheader("AI Match Predictions")

            for r in range(len(names) - 1):
                st.write(f"### Round {r + 1}")

                for i in range(len(names) // 2):
                    a, b = names[i], names[-1 - i]

                    if a != "BYE" and b != "BYE":
                        result = model.predict(
                            pd.DataFrame(
                                [[points[a], points[b]]],
                                columns=["home_points", "away_points"]
                            )
                        )[0]

                        prediction = {
                            "H": a + " may win",
                            "D": "Possible draw",
                            "A": b + " may win"
                        }

                        st.write(f"⚽ {a} vs {b}")
                        st.write("AI:", prediction[result])

                names = (
                    [names[0]] + [names[-1]] + names[1:-1]
                )

    except (ValueError, KeyError):
        st.error("Enter valid data: Team Name,Points")
