import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import os

teams = {
    "Team 1": {"members": ["Ailidh Snook", "Ashleigh Wilcox", "Amber Vater", "Nicole Ashman"], "steps": [], "calories": []},
    "Team 2": {"members": ["Becky Lyons-Helps", "Nikki Cholod", "Sian Giles-Titcombe", "Felcy Fernandes", "Maggie Wilson"], "steps": [], "calories": []},
    "Team 3": {"members": ["Sarah Garlick", "Jane Long", "Mel Kidd", "Rachel Reynolds"], "steps": [], "calories": []},
}

st.set_page_config(page_title="Step Challenge", layout="wide")

challenge_image = "images/step_challenge.jpg"  
if os.path.isfile(challenge_image):
    st.image(challenge_image, use_column_width=True)
else:
    st.warning("Image not found.")

st.title("Step Challenge App - 1 Hour Fitness Challenge")

team_name = st.selectbox("Select Your Team", list(teams.keys()))

member_name = st.selectbox("Select Your Name", teams[team_name]["members"])

steps = st.number_input("Enter Steps Walked", min_value=0, value=0, step=100)

calories = steps * 0.04

if st.button("Submit Data"):
    teams[team_name]["steps"].append(steps)
    teams[team_name]["calories"].append(calories)
    st.success(f"{member_name} added {steps} steps and burned {calories:.2f} calories!")

st.header(f"{team_name} - Statistics")
if teams[team_name]["steps"]:
    df = pd.DataFrame({"Steps": teams[team_name]["steps"], "Calories": teams[team_name]["calories"]})
    st.dataframe(df)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    
    ax[0].plot(df["Steps"], marker="o", linestyle="-", color="blue", label="Steps")
    ax[0].set_title("Steps Progress")
    ax[0].set_ylabel("Steps")
    ax[0].legend()
    
    ax[1].plot(df["Calories"], marker="o", linestyle="-", color="red", label="Calories")
    ax[1].set_title("Calories Burned")
    ax[1].set_ylabel("Calories")
    ax[1].legend()
    
    plt.tight_layout()  
    st.pyplot(fig)

motivational_quotes = [
    "Keep going! Every step counts!",
    "You're doing great! Stay active!",
    "One step at a time! Keep moving!",
]
st.subheader(random.choice(motivational_quotes))
