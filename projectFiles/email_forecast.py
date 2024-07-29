# email_forecast.py
import os, requests
import smtplib
from datetime import datetime
import schedule
import time
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

MY_EMAIL = os.getenv('GMAIL')    # Replace with your email address
MY_PASSWORD = os.getenv('GMAIL_PASSWORD')          # Replace with your password


if not MY_EMAIL:
    print("getting env vars failed")
else:
    print(f"Loaded GMAIL: {MY_EMAIL}")
    print(f"Loaded GMAIL_PASSWORD: {MY_PASSWORD}")
    
MY_LATITUDE = 40.6401
MY_LONGITUDE = 22.9444
URL = f"https://api.open-meteo.com/v1/forecast?latitude={MY_LATITUDE}&longitude={MY_LONGITUDE}&daily=weathercode,temperature_2m_max&timezone=Europe%2FBerlin"
EMAIL_LIST_FILE = 'email_list.txt'
def getting_temp():
    temporary = requests.get(url=URL)
    data = temporary.json()
    temp_today = data["daily"]["temperature_2m_max"][0]
    return temp_today

def get_email_list(filename):
    with open(filename, 'r') as file:
        emails = file.read().splitlines()
    return emails

def send_daily_email():
    temp = getting_temp()
    clients = get_email_list(EMAIL_LIST_FILE)
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            print("Login successful")
    except Exception as e:
        print(f"Login failed: {e}")
            for client in clients:
                message = f"Subject: Today's temperature {temp}C\n\nThe highest temperature today is going to be {temp}C. Enjoy your day."
                connection.sendmail(MY_EMAIL, client, message)
        print(f"Emails sent successfully at {datetime.now()}")
    except Exception as e:
        print(f"An error occurred: {e}")


schedule.every().day.at("14:29").do(send_daily_email)


while True:
    schedule.run_pending()
    time.sleep(1)
