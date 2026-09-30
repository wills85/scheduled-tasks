import requests
from twilio.rest import Client
import json
import os

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 51.625678,
    "lon": -0.108535,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        content_sid="HXfe5ab5f00277942d4d4200328b4d403c",
        content_variables=json.dumps({"1": "Today", "2": "Rain expected"}),
        from_="whatsapp:+447723317807",
        to="whatsapp:+447842563897",
    )

    print(message.status)
