"""

A fun and interesting script that prints current forecast / weather
information for any location on Earth.

First you enter a location or street name
    e.g., Buckingham Palace
    e.g., Rue de Rivoli
    e.g., Hollywood Blvd Los Angeles

The script calls Geocoding API to get latitude and longtitude coordinates.

Then the script calls a weather API to get forecast details for the 
given coordinates.

"""

import urllib
import requests
from requests.structures import CaseInsensitiveDict
import pendulum
import getstring
"""
    Install a required module dynamically
    print("pip install pendulum (if not already installed)")
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pendulum'])
    import pendulum
"""

WEATHER_API  =  'https://api.met.no/weatherapi/locationforecast/2.0/compact'
headers_met  = {}
headers_met['User-Agent'] =  'Testing out forecasting API'

coordinates = {}

# Prompt user for location
location = getstring.get("Please enter a location on planet Earth:  ", default="Buckingham Palace")
my_params = {'text': location, 'apiKey': "610e4bc5f6c74b8b9376bca934724022"}

# Convert location to lat and lon
url_geo = "https://api.geoapify.com/v1/geocode/search?"
url_geo = url_geo + urllib.parse.urlencode(my_params)
print("\nCall geocoding API...")
headers_geo = CaseInsensitiveDict()
headers_geo["Accept"] = "application/json"
response_geo = requests.get(url_geo, headers=headers_geo)
print(response_geo.status_code)
try:
    formatted_location = response_geo.json()['features'][0]['properties']['formatted']
    geo_timezone = response_geo.json()['features'][0]['properties']['timezone']['name']
    coordinates['lon'] = response_geo.json()['features'][0]['bbox'][0]
    coordinates['lat'] = response_geo.json()['features'][0]['bbox'][1]

    print(f"Call weather API with coordinates {coordinates}")
    response_met  =  requests.get(WEATHER_API, headers=headers_met, params=coordinates)
    print(response_met.status_code)

    forecast  =  response_met.json()['properties']['timeseries'][0]
#    print(forecast)
    time  = pendulum.parse(forecast['time'])
    localtime  =  time.in_timezone(geo_timezone) # You can change this to your local timezone see 'TZ identifier' here: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    celsius    =  forecast['data']['instant']['details']['air_temperature']
    fahrenheit = (celsius  *  9/5) +  32
    humidity   = forecast['data']['instant']['details']['relative_humidity'] 
    windspeed  = forecast['data']['instant']['details']['wind_speed']
    symbol1    = forecast['data']['next_1_hours']['summary']['symbol_code']
    symbol6    = forecast['data']['next_6_hours']['summary']['symbol_code']

    print(f"\nLocation is: {formatted_location}")
    print(f"Local timezone is: {geo_timezone}")
    print(f"Local time to nearest hour: {localtime.format('dddd Do [of] MMMM YYYY h:mm A')}")
    print("Forecast is:")
    print(f"  Air temperature: {celsius} degrees Celsius ({round(fahrenheit, 2)} degrees Fahrenheit)")
    print(f"  Relative humidity: {humidity} %")
    print(f"  Wind speed: {windspeed} m/s")
    print(f"  Next hour: {symbol1}")
    print(f"  Next six hours: {symbol6}")

except IndexError:
    print(f"Did not find location {location} in the Geocoding API database")

#EOF
