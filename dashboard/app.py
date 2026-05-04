import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv("data/healthcare_dataset.csv")

# nettoyage (OBLIGATOIRE)
df.columns = [re.sub(r'[^a-zA-Z0-9_]', '', col.replace(" ", "_")) for col in df.columns]

st.title("Healthcare Monitoring Dashboard")

st.subheader("Dataset")
st.dataframe(df)

st.subheader("Heart Rate Distribution")

fig, ax = plt.subplots()
df["Heart_Rate_bpm"].plot(kind="hist", bins=20, ax=ax)
st.pyplot(fig)

st.subheader("Average Values")

st.write("Heart Rate:", df["Heart_Rate_bpm"].mean())
st.write("Temperature:", df["Body_Temperature_C"].mean())   
st.write("SpO2:", df["SpO2_Level_"].mean())                 