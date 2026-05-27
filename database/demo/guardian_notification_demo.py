def send_guardian_notification(alert_type, elderly_name, severity):
    message = {
        "to": "guardian@example.com",
        "elderly_user": elderly_name,
        "alert_type": alert_type,
        "severity": severity,
        "status": "sent"
    }
    return message


alert = send_guardian_notification(
    alert_type="Fall Detection",
    elderly_name="Mr. Chen",
    severity="High"
)

print("Guardian Notification")
print("---------------------")
print("To:", alert["to"])
print("Elderly User:", alert["elderly_user"])
print("Alert Type:", alert["alert_type"])
print("Severity:", alert["severity"])
print("Status:", alert["status"])
