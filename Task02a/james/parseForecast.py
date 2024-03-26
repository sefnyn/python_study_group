#!/usr/bin/env python3
import  json
import pendulum

with open('forecast.json') as f:
    response = json.load(f)

forecast = response['properties']['timeseries'][0]

time  = pendulum.parse(forecast['time'])
localtime  =  time.in_timezone('America/New_York')

celsius  =  forecast['data']['instant']['details']['air_temperature']
farenheit  = round((celsius  *  9/5) +  32, 1)

output =  f"At {localtime.format('dddd Do [of] MMMM YYYY h:mm A')}, "
output += f"it was {celsius}° Celsius (that's {farenheit}° Farenheit)"
print(output)