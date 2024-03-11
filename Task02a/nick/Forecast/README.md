# Current forecast of any city or town

## Usage
$ ./bin/python3 forecast.py

Please enter a location in the format 'City/Town, Country':   [Default: Durham, UK]: 

Call geo API... https://api.geoapify.com/v1/geocode/search?text=Durham%2C+UK&apiKey=610e4bc5f6c74b8b9376bca934724022  
200  
Call weather API... https://api.met.no/weatherapi/locationforecast/2.0/compact  
200  
pip install pendulum (if not already installed)  
Requirement already satisfied: pendulum in ./lib/python3.11/site-packages (3.0.0)  
Requirement already satisfied: python-dateutil>=2.6 in ./lib/python3.11/site-packages (from pendulum) (2.9.0.post0)  
Requirement already satisfied: tzdata>=2020.1 in ./lib/python3.11/site-packages (from pendulum) (2024.1)  
Requirement already satisfied: time-machine>=2.6.0 in ./lib/python3.11/site-packages (from pendulum) (2.14.0)  
Requirement already satisfied: six>=1.5 in ./lib/python3.11/site-packages (from python-dateutil>=2.6->pendulum) (1.16.0)  

Local timezone is: Europe/London  
In the location Durham, DH1 3NG, United Kingdom, and on Monday 11th of March 2024 4:00 PM it is 7.0 degrees celsius (that's 44.6 degrees farenheit)
