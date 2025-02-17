import requests
import json

# print(json.__version__)

BASE_URL = "https://api.openweathermap.org/data/3.0/onecall?"

def build_request(lat, lon, API, exclude=""):
    return BASE_URL+"lat="+lat+"&lon="+lon+"&exclude="+exclude+"&appid="+API    