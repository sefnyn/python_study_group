# Current forecast of any city or town

## Usage
$ ./bin/python3 forecast.py

Please enter a location on planet Earth:   [Default: Buckingham Palace]  

Call geocoding API... https://api.geoapify.com/v1/geocode/search?text=Buckingham+Palace&apiKey=610e4bc5f6c74b8b9376bca934724022  
200  
Call weather API... https://api.met.no/weatherapi/locationforecast/2.0/compact  
200  

Location is: Buckingham Palace, Buckingham Gate, London, SW1A 1AA, United Kingdom  
Local timezone is: Europe/London  
Local time to nearest hour: Tuesday 12th of March 2024 12:00 PM  
Forecast is:  
>  Air temperature: 11.4 degrees Celsius (52.52 degrees Fahrenheit)  
>  Relative humidity: 91.3 %  
>  Wind speed: 5.7 m/s  
>  Next hour: heavyrain  
>  Next six hours: rain  
