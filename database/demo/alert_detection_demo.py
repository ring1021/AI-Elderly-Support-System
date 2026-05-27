heart_rate = 125
fall_detected = True
door_open = False

if heart_rate > 120:
    print("High heart rate alert triggered.")

if fall_detected:
    print("Fall detected. Sending emergency alert.")

if door_open:
    print("Warning: Door left open.")
