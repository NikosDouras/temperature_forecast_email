import os
import requests
import smtplib
from datetime import datetime
import schedule
import time
from dotenv import load_dotenv


load_dotenv()

MY_EMAIL = os.getenv('GMAIL')
MY_PASSWORD = os.getenv('GMAIL_PASSWORD')

if not MY_EMAIL or not MY_PASSWORD:
    print("Getting env vars failed")
else:
    print(f"Loaded GMAIL: {MY_EMAIL}")

MY_LATITUDE = 40.6401
MY_LONGITUDE = 22.9444
URL = f"https://api.open-meteo.com/v1/forecast?latitude={MY_LATITUDE}&longitude={MY_LONGITUDE}&daily=weathercode,temperature_2m_max&timezone=Europe%2FBerlin"
EMAIL_LIST_FILE = 'email_list.txt'


def getting_temp():
    response = requests.get(url=URL)
    data = response.json()
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

            for client in clients:
                message = f"Subject: Today's temperature {temp}C\n\nThe highest temperature today is going to be {temp}C. Enjoy your day."
                connection.sendmail(MY_EMAIL, client, message)
            print(f"Emails sent successfully at {datetime.now()}")

    except Exception as e:
        print(f"An error occurred: {e}")

# while True:
#     print("Waiting 1 minute")
#     time.sleep(30)
#     print("Sending Emails")
#     send_daily_email()
# Schedule the task
schedule.every().day.at("14:29").do(send_daily_email)
send_daily_email()

while True:
    schedule.run_pending()
    time.sleep(1)
