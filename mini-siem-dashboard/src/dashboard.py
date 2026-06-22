

import streamlit as st
import pandas as pd

from parser import parse_logs
from detector import detect_alerts

logs = parse_logs("logs/sample.log")

alerts = detect_alerts(logs)

st.title("Mini SIEM Dashboard")

st.header("Log Statistics")

total_logs = len(logs)

error_logs = len(
    [log for log in logs if log["level"] == "ERROR"]
)

warning_logs = len(
    [log for log in logs if log["level"] == "WARNING"]
)

st.metric("Total Logs", total_logs)
st.metric("Errors", error_logs)
st.metric("Warnings", warning_logs)

st.header("Alerts")

for alert in alerts:
    st.error(alert)

df = pd.DataFrame(logs)

st.header("Log Distribution")

st.bar_chart(
    df["level"].value_counts()
)

st.header("Raw Logs")

st.write(logs)

import time

placeholder = st.empty()

while True:

    logs = parse_logs("logs/sample.log")

    placeholder.write(logs)

    time.sleep(5)
