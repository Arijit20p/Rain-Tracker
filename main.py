import requests
from twilio.rest import Client
import os

account_sid = "AC9cad0555bc61f41f5c9c216a2d032f6d"
auth_token = "36e553d9d2838b9ceafc279c8dbb5ce4"

api_key = "910fcfb8195f35f65a1fa7811d8fbb5e"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
data_params = {
    "lat": 22.841150,
    "lon": 88.126373,
    "appid": api_key,
    "cnt": 4

}

will_rain = False
response = requests.get(url=OWN_ENDPOINT, params=data_params)
response.raise_for_status()
data = response.json()
# data_id = data["list"][0]["weather"][0]["id"]
# print(data_id)
# print(type(data_id))
list_of_weather_id = []
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if condition_code < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_="+13125483660",
    body="It's raining. Remember to bring an umbrella",
    to="+919123355190"
    )
    print(message.status)

