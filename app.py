import pandas as pd
import plotly.express as px
import streamlit as st

from grades import gpa_points, subject_average, weighted_gpa

st.title("Student Grade Calculator")

if "subjects" not in st.session_state:
    st.session_state.subjects = {}

subjects = st.session_state.subjects

# ---- Add subject ----
st.header("Add subject")
name = st.text_input("Subject name")
credits = st.number_input("Credits", value=3)
if st.button("Add subject"):
    subjects[name] = {"credits": credits, "grades": []}

# ---- Add grade ----
st.header("Add grade")
if subjects:
    subject = st.selectbox("Subject", list(subjects.keys()))
    grade = st.number_input("Grade (0-100)", value=0.0)
    if st.button("Add grade"):
        subjects[subject]["grades"].append(grade)
else:
    st.info("Add a subject first.")

# ---- Results ----
st.header("Results")
rows = []
for subject_name, data in subjects.items():
    avg = subject_average(data["grades"])
    points = gpa_points(avg)
    rows.append(
        {
            "Subject": subject_name,
            "Credits": data["credits"],
            "Average": round(avg, 2),
            "GPA points": points,
        }
    )

if rows:
    df = pd.DataFrame(rows)
    st.dataframe(df)

    gpa = weighted_gpa([(r["GPA points"], r["Credits"]) for r in rows])
    st.metric("GPA (4.0 scale)", round(gpa, 2))

    # ---- Charts ----
    st.header("Performance")
    st.plotly_chart(px.bar(df, x="Subject", y="Average", title="Average by subject"))

    history = []
    for subject_name, data in subjects.items():
        for i, g in enumerate(data["grades"], start=1):
            history.append({"Subject": subject_name, "Entry #": i, "Grade": g})
    if history:
        st.plotly_chart(
            px.line(pd.DataFrame(history), x="Entry #", y="Grade", color="Subject", markers=True,
                    title="Grades over time")
        )
