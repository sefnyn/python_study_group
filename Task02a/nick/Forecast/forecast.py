import urllib
import requests
from requests.structures import CaseInsensitiveDict
import getstring

url_met  =  'https://api.met.no/weatherapi/locationforecast/2.0/compact'
headers_met  = {}
headers_met['User-Agent'] =  'Testing out forecasting API'

params  = {}
"""
params['lat'] =  -37.81002731164721  #Melbourne
params['lon'] =  144.96436660091567

params['lat'] =  54.77676  #Durham
params['lon'] =  -1.57566

params['lat'] = getfloating.get("Enter latitude: ", default=54.77676)
params['lon'] = getfloating.get("Enter longtitude: ", default=-1.57566)
"""

# Prompt user for location
location = getstring.get("Please enter a location in the format 'City/Town, Country':  ", default="Durham, UK")
my_params = {'text': location, 'apiKey': "610e4bc5f6c74b8b9376bca934724022"}

# Convert location to lat and lon
url_geo = "https://api.geoapify.com/v1/geocode/search?"
url_geo = url_geo + urllib.parse.urlencode(my_params)
print("Call geo API...", url_geo)
headers_geo = CaseInsensitiveDict()
headers_geo["Accept"] = "application/json"
response_geo = requests.get(url_geo, headers=headers_geo)
print(response_geo.status_code)
try:
    formatted_location = response_geo.json()['features'][0]['properties']['formatted']
    geo_timezone = response_geo.json()['features'][0]['properties']['timezone']['name']
    params['lon'] = response_geo.json()['features'][0]['bbox'][0]
    params['lat'] = response_geo.json()['features'][0]['bbox'][1]

    print("Call weather API...", url_met)
    response_met  =  requests.get(url_met, headers=headers_met, params=params)
    print(response_met.status_code)
#print(response_met.json())
#print(f"\nUrl is {response_met.url}")

    forecast  =  response_met.json()['properties']['timeseries'][0]
#print("Forecast: ", forecast)

    print("pip install pendulum (if not already installed)")
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pendulum'])
    import pendulum
    time  = pendulum.parse(forecast['time'])
    localtime  =  time.in_timezone(geo_timezone) # You can change this to your local timezone see 'TZ identifier' here: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
#print(localtime)
    celsius  =  forecast['data']['instant']['details']['air_temperature']
    farenheit  = (celsius  *  9/5) +  32
#print(farenheit)

    print(f"\nLocal timezone is: {geo_timezone}")
    print(f"In the location {formatted_location}, and on {localtime.format('dddd Do [of] MMMM YYYY h:mm A')} it is {celsius} degrees celsius (that's {round(farenheit, 2)} degrees farenheit)")
except IndexError:
    print(f"Did not find location {location} in the Geocoding API database")
