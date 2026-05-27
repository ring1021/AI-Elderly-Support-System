reminders = [
    {"type": "Medication", "time": "08:00", "message": "Take morning medicine"},
    {"type": "Appointment", "time": "14:30", "message": "Doctor appointment"},
    {"type": "Bill", "time": "18:00", "message": "Pay electricity bill"}
]

print("Reminder List")
print("-------------")

for reminder in reminders:
    print(reminder["time"], "-", reminder["type"], "-", reminder["message"])

user_action = "acknowledged"

if user_action == "acknowledged":
    print("\nReminder status: acknowledged by elderly user.")
elif user_action == "postponed":
    print("\nReminder status: postponed.")
else:
    print("\nReminder status: skipped.")
