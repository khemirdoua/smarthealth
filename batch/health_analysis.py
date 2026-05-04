import pandas as pd
import re

df = pd.read_csv("data/healthcare_dataset.csv")

df.columns = [re.sub(r'[^a-zA-Z0-9_]', '', col.replace(" ", "_")) for col in df.columns]

print("=== Batch Analysis ===")

print("Average Heart Rate:", df["Heart_Rate_bpm"].mean())
print("Average Temperature:", df["Body_Temperature_C"].mean())
print("Average SpO2:", df["SpO2_Level_"].mean())

critical = df[
    (df["Heart_Rate_bpm"] > 100) |
    (df["Body_Temperature_C"] > 38) |
    (df["SpO2_Level_"] < 90)
]

print("Critical patients:", len(critical))