import requests
import smtplib

MY_EMAIL="ur_mail"
MY_PASSWORD="password"

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key="5852c4c0d510e3e5911cb3f817af06f9"
weather_params={
    "lat":"ur_lat",
    "lon":"ur_lon",
    "appid":api_key,
    "cnt":4,
}

response=requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data=response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    print("Bring an umbrella.")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Bring Umbrella "
        )







