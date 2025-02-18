import requests
from dotenv import dotenv_values

# load_dotenv()

config = dotenv_values(".env")

BASE_URL = "https://api.openweathermap.org/data/3.0/onecall"

# print(json.__version__)

# print(config["APIKEY"])


# def build_request(lat, lon, API, exclude=""):
#     return BASE_URL+"lat="+lat+"&lon="+lon+"&exclude="+exclude+"&appid="+API

columbia_lat = 34.00071
columbia_long = -81.03481

payload = {
    'lat': columbia_lat,
    'lon':columbia_long,
    'appid':config["APIKEY"],
    'exclude':'minutely,hourly,daily,alerts',
    'units':'imperial'
}

# request_url = build_request(columbia_lat, columbia_long, config["APIKEY"])

req = requests.get(BASE_URL, params=payload)

# print(req.url)

data = req.json()

weather = data['current']

if (weather['temp'] > 70):
    print("Warm")
elif (weather['temp'] > 50):
    print("midweather")
elif (weather['temp'] > 30):
    print('pretty cold')
else:
    print('absolutely freezing')