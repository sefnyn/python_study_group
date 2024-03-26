#!/usr/bin/env python3
import  requests
import json

url  =  'https://api.met.no/weatherapi/locationforecast/2.0/compact'

headers  = {}
headers['User-Agent'] =  'Testing out forecasting API'

params  = {} # Coordinates for Swarthmore PA
params['lat'] =  39.901667
params['lon'] =  -75.346944

response  =  requests.get(url, headers=headers, params=params)
print(response.json())
print(f"\nUrl is {response.url}")

print('Writing results to JSON...')
with open('forecast.json', 'w') as f:
    json.dump(response.json(), f)
print('Data successfully written to JSON file.')