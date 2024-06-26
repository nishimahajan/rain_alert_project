import requests
from twilio.rest import Client
api_key = "c105b79fe00670ad0eb58ac9dc01054f"
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
chd_lat = 30.733315
chd_lon = 76.779419
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxx"

weather_params = {
    "lat": chd_lat,
    "lon": chd_lon,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
# print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella!",
        from_='+16562315897',
        to='+919914522254'
    )
    print(message.status)
elif not will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's not going to rain today. No Umbrella Needed!",
        from_='+16562315897',
        to='+919914522254'
    )
    print(message.status)
