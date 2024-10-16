import requests
import time
import sqlite3
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
# from smtplib import SMTP  # for email alerts

API_KEY = 'your_openweathermap_api_key'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Function to retrieve weather data
def get_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

# Function to convert temperature
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to calculate daily summary
def calculate_daily_summary(weather_data):
    df = pd.DataFrame(weather_data)
    avg_temp = df['temp'].mean()
    max_temp = df['temp'].max()
    min_temp = df['temp'].min()
    dominant_condition = df['main'].mode()[0]  # Most frequent weather condition
    return avg_temp, max_temp, min_temp, dominant_condition

# Function to store daily summary in the database
def store_daily_summary(city, date, avg_temp, max_temp, min_temp, dominant_condition):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS daily_summary (
                      city TEXT, date TEXT, avg_temp REAL, max_temp REAL, 
                      min_temp REAL, dominant_condition TEXT)''')
    cursor.execute('''INSERT INTO daily_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                      (city, date, avg_temp, max_temp, min_temp, dominant_condition))
    conn.commit()
    conn.close()

# Alerting system
def check_alert_conditions(current_temp, threshold_temp, city):
    if current_temp > threshold_temp:
        print(f"ALERT: {city} temperature exceeded {threshold_temp}°C!")

# Main execution loop
def main():
    threshold_temp = 35  # User-defined alert threshold
    weather_data_per_day = []

    while True:
        current_time = datetime.now().strftime("%Y-%m-%d")
        for city in CITIES:
            weather = get_weather_data(city)
            temp_celsius = kelvin_to_celsius(weather['main']['temp'])
            weather_data_per_day.append({
                'city': city,
                'date': current_time,
                'temp': temp_celsius,
                'main': weather['weather'][0]['main'],
            })
            check_alert_conditions(temp_celsius, threshold_temp, city)

        if len(weather_data_per_day) >= len(CITIES) * 24:  # Assuming data collected hourly for 1 day
            avg_temp, max_temp, min_temp, dominant_condition = calculate_daily_summary(weather_data_per_day)
            for city in CITIES:
                store_daily_summary(city, current_time, avg_temp, max_temp, min_temp, dominant_condition)
            weather_data_per_day.clear()  # Reset for next day

        time.sleep(300)  # Sleep for 5 minutes (300 seconds)

if __name__ == "__main__":
    main()
