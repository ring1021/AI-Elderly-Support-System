elderly_profile = {
    "name": "Mr. Chen",
    "age": 78,
    "status": "active"
}

latest_vitals = {
    "heart_rate": 118,
    "temperature": 28,
    "humidity": 65,
    "fall_detected": False,
    "door_open": True
}

print("Guardian Dashboard")
print("------------------")
print("Elderly User:", elderly_profile["name"])
print("Age:", elderly_profile["age"])
print("Status:", elderly_profile["status"])

print("\nLatest Sensor Data:")
for key, value in latest_vitals.items():
    print(key, ":", value)

if latest_vitals["door_open"]:
    print("\nAlert: Door is currently open.")
