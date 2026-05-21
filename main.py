import requests
import os
import smtplib

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")


api_key = os.environ.get("API_KEY")
parameters = {
    'lat': 5.359952,
    'lon': -4.008256,
    'appid': api_key,
    'cnt': 4,
}
url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=url, params=parameters)
response.raise_for_status()
weather_data = response.json()
# rain = weather_data[0]['weather'][0]['id']

will_rain = False
for item in weather_data["list"]:
    weather_id = item['weather'][0]['id']
    weather_name = item['weather'][0]['main']

    if weather_id < 700 :
        will_rain = True


if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject : Hey Brother !! \n\n Its going to rain today Remember to Bring your Umbrella !!"
        )

