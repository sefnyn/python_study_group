# Current forecast of any location

## Usage
Clone the repo.  
Create a virtual environment for the code.  
Install 3rd party modules:  requests and pendulum  

$ ./bin/python3 forecast.py

Global weather forecasting system  
---------------------------------  
Please enter a location on planet Earth:   [Default: Buckingham Palace]   

Call geocoding API...  
200  
Call weather API with coordinates {'lon': -0.144018, 'lat': 51.4997246}  
200  

Location is: Buckingham Palace, Buckingham Gate, London, SW1A 1AA, United Kingdom  
Local timezone is: Europe/London  
Local time to nearest hour: Tuesday 12th of March 2024 2:00 PM  
Forecast is:  
>  Air temperature: 12.2 degrees Celsius (53.96 degrees Fahrenheit)  
>  Relative humidity: 88.8 %  
>  Wind speed: 6.7 m/s  
>  Next hour: cloudy  
>  Next six hours: cloudy  

Fetch another forecast?  (y/n) [Default: y] n  
Thank you for using the Global weather forecasting system!  
