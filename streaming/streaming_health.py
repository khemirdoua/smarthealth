from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'health-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Monitoring patients...")

for message in consumer:
    data = message.value

    alerts = []

    if data["heart_rate"] > 100:
        alerts.append("High Heart Rate")

    if data["temperature"] > 38:
        alerts.append("Fever")

    if data["spo2"] < 90:
        alerts.append("Low Oxygen")

    if data["systolic_bp"] > 140:
        alerts.append("High Blood Pressure")

    if alerts:
        print(f"ALERT for {data['patient_id']}:", alerts)
    else:
        print(f"OK: {data['patient_id']}")