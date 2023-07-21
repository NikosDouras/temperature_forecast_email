import requests
import smtplib

MY_EMAIL =              #Add your email address (make a new one if needed)
MY_PASSWORD =           #Add your password. You can make one for general use, at least on gmail.
CLIENT =                #Add email address of recipient
MY_LATITUDE = 40.629269 #Change long and lat for different cities.
MY_LONGITUDE = 22.947412
URL = "https://api.open-meteo.com/v1/" \
      f"forecast?latitude={MY_LATITUDE}&longitude={MY_LONGITUDE}&daily=weathercode,temperature_2m_max&timezone=Europe%2FBerlin"

def getting_temp():
    temporary = requests.get(url=URL)
    data = temporary.json()
    temp_today = data["daily"]["temperature_2m_max"][0]

    return temp_today


def sending_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        temp = getting_temp()
        connection.sendmail(MY_EMAIL, CLIENT, msg=f"Subject:today's temperature {temp}C \n\nThe highest temperature"
                                                  f" today is going to be {temp}C. Enjoy your day.")


sending_email()