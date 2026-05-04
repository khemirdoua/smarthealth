from kafka import KafkaProducer
import pandas as pd
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

df = pd.read_csv("data/healthcare_dataset.csv")

# nettoyage colonnes
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace("(", "")
df.columns = df.columns.str.replace(")", "")
df.columns = df.columns.str.replace("%", "")
df.columns = df.columns.str.replace("°C", "")

print("Streaming data...")

for _, row in df.iterrows():
    data = {
        "patient_id": row["Patient_Number"],
        "heart_rate": row["Heart_Rate_bpm"],
        "spo2": row["SpO2_Level_"],
        "temperature": row["Body_Temperature"],
        "systolic_bp": row["Systolic_Blood_Pressure_mmHg"],
        "diastolic_bp": row["Diastolic_Blood_Pressure_mmHg"]
    }

    producer.send("health-topic", data)
    print("Sent:", data)

    time.sleep(1)

producer.flush()