import streamlit as st
from datetime import timedelta, datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

st.title("🎓 Candidacy Date Backtracker & Timeline")

# 1) Pick your oral exam date via calendar
oral = st.date_input("Select your Oral Exam Date")

if oral:
    # 2) Compute the other key dates
    written     = oral - timedelta(days=14)
    sched_start = written - timedelta(days=21)
    sched_end   = written - timedelta(days=14)
    proposal    = oral - timedelta(days=14)

    dates = {
        "Written Exam":          written,
        "Sched. Request Start":  sched_start,
        "Sched. Request End":    sched_end,
        "Proposal to Committee": proposal,
        "Oral Exam":             oral,
    }

    # 3) Show the dates as text
    st.markdown("---")
    for label, d in dates.items():
        st.write(f"**{label:22s}:** {d}")

    # 4) Show the dates on a timeline
    st.markdown("---")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.set_title("Key Dates Timeline")
    ax.set_xlabel("Date")
    ax.set_ylabel("Event")