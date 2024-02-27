import sys 
import subprocess

subprocess.check_call([sys.executable, '-m','pip','install','pendulum'])

import requests
import pendulum


#api call 
url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'

headers = {}
headers['User-Agent'] = 'Testing out forcasting API'

params = {}
params['lat'] = 42.383333 #-37.81002731164721
params['lon'] = -72.516667 #144.96436660091567

response = requests.get(url, headers=headers, params=params)
##print(response.json())
print(f"\nUrl is {response.url}")


##print(response.json()['properties']['timeseries'][0])
forecast = response.json()['properties']['timeseries'][0]

time = pendulum.parse(forecast['time'])
localtime = time.in_timezone('America/New_York') #use this to change the local timezone
#see 'TZ identifier' here: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

print(localtime)

celsius = forecast['data']['instant']['details']['air_temperature']
farenheit = (celsius * 9/5) + 32
print(farenheit)
print(round(farenheit,2))

print(f"At {localtime.format('dddd Do [of] MMMM YYYY h:mm A')} it was {celsius} degrees celsius (that's {round(farenheit, 2)} degrees farenheit)")