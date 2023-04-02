import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "401eec078d7e7ac9819450cb08497dd7"

weather_params = {
    "lat":38.627003,
    "lon":-90.199402,
    "appid":api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:4]

will_rain = False

#Each 'slice' in 'weather_slice' is a 3 hour interval
for hour_data in weather_slice:
    print(hour_data["weather"][0])
    condition_code = hour_data["weather"][0]["id"]
    #print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain == True:
    print("Looks like rain today boyzzzz, bring an umbrella with you!")
else:
    print("Weather looks dry for the day, no need for an umbrella BOYZZZZ!!")
    





