import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "401eec078d7e7ac9819450cb08497dd7"

account_sid = "AC4f76975f683b0c86d385c1f0749e3779"
auth_token = "c9d7f5d75bcd34ab51ca9f2fb78e3752"
# auth_token = os.environ["c9d7f5d75bcd34ab51ca9f2fb78e3752"]

weather_params = {
    "lat":38.6272700,
    "lon":-90.1978900,
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
    #print("Looks like rain today boyzzzz, bring an umbrella with you!")
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="Looks like rain today boyzzzz, bring an umbrella with you!☂️",
        from_="+18442923991",
        to="+16185415179"
    )
    print(message.status)
# else:
#     #print("Weather looks dry for the day, no need for an umbrella BOYZZZZ!!")
#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https': os.environ['https_proxy']}
#     client = Client(account_sid, auth_token, http_client=proxy_client)
#     message = client.messages.create(
#         body="Weather looks dry for the day, no need for an umbrella BOYZZZZ!!",
#         from_="+18442923991",
#         to="+16185415179"
#     )
#     print(message.status)
