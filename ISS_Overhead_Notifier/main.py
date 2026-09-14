import requests
from datetime import datetime
import smtplib

MY_EMAIL="yourmail"
MY_PASSWORD="yourpassword"
MY_LAT = 20.047123
MY_LONG = 74.481873

def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()

    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude=float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <=MY_LAT+5 and MY_LONG-5<= iss_longitude <=MY_LONG+5:
           return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted":0
    }

    response = requests.get("https://api.sunrise-sunset.org/v2", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])
    time_now=datetime.now().hour

    if time_now>=sunset or time_now<=sunrise:
        return True

while True:
    if is_iss_overhead() &  is_night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )
