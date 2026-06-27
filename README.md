# AI Elderly Support System

## Project Overview

This project is an AI-assisted elderly support system designed to monitor the health and safety of elderly individuals living alone.  
The system integrates wearable sensor simulation, environmental monitoring, alert generation, and caregiver notification modules.

The system is implemented using a simulation-based architecture to demonstrate real-time monitoring, event detection, and alert communication without requiring physical hardware.

---

## Repository Structure
AI-Elderly-Support-System/
│
├── database/
│ ├── demo/
│ │ ├── sample_sensor_data.json
│ │ ├── alert_detection_demo.py
│ │ ├── guardian_notification_demo.py
│ │ ├── reminder_demo.py
│ │ └── guardian_dashboard_demo.py
│ │
│ └── schema.sql
│
├── README.md
├── LICENSE
└── .gitignore
---

## System Modules

### 1. Sensor Data Simulation
Simulates wearable and environmental sensor data, including:
- Heart rate
- Step count
- Temperature
- Humidity
- Door status

---

### 2. Alert Detection Module
Implements rule-based logic to detect abnormal events such as:
- High/low heart rate
- Sudden inactivity (fall risk)
- Extreme environmental conditions
- Door left open for extended time

---

### 3. Guardian Notification Module
Generates real-time alerts for caregivers when abnormal events are detected.  
Supports priority-based classification of alerts.

---

### 4. Database Module
Stores:
- Sensor readings
- User information
- Alert logs
- System events

Database schema is defined in `schema.sql`.

---

### 5. Dashboard Simulation
Provides a simulated interface for:
- Elderly user view
- Caregiver monitoring view
- Alert visualization
- Historical data tracking

---

## Technologies Used

- Python 3.x
- SQLite / SQL-based database schema
- JSON for sensor data simulation
- Rule-based event detection logic

---

## How to Run the Project


### 1. Clone Repository

```bash
git clone https://github.com/ring1021/AI-Elderly-Support-System.git
cd AI-Elderly-Support-System
```

### 2. Initialize Database

```bash
sqlite3 database.db < database/demo/schema.sql
```

### 3. Run Sensor Simulation

```bash
python database/demo/alert_detection_demo.py
```

### 4. Run Alert System

```bash
python database/demo/guardian_notification_demo.py
```

### 5. Run Dashboard Demo

```bash
python database/demo/guardian_dashboard_demo.py
```
