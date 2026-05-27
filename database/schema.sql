CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(20),
    contact_info VARCHAR(100)
);

CREATE TABLE Devices (
    device_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id),
    device_type VARCHAR(50),
    status VARCHAR(20)
);

CREATE TABLE Alerts (
    alert_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id),
    alert_type VARCHAR(50),
    alert_time TIMESTAMP,
    status VARCHAR(20)
);
