# Find a Restaurant

An application that finds a resturant given a location and
a query string. 

It makes API requests to Google Maps' Geolocation API and 
Foursquare's Search and Venue Photos API.

## Prerequisites

1. python
2. python libraries: json, httplib2, sys, codecs
3. `geocode.py`
4. `findARestaurant.py`
5. Google developer account
6. Google API key
6. Foursquare developer account
8. Foursquare API client ID and client secret
9. `client_secrets.json` with the Google API key, Foursquare client
ID and client secret fields filled in 

#### How to get a Google API key
_To follow_

#### How to get a Foursquare API client ID and secret
_To follow_

## Usage

The following resource gives more information on how to run python scripts: 
[How to Run a Python Script via a File or the Shell](https://www.pythoncentral.io/execute-python-script-file-shell/).

Run the script `findARestaurant.py`.

It will return one restaurant's name, address and image URL for each of the 
following sets of parameters:
1. Pizza in Tokyo, Japan
2. Tacos in Jakarta, Indonesia
3. Tapas in Maputo, Mozambique
4. Falafel in Cairo, Egypt
5. Spaghetti in New Delhi, India
6. Cappuccino in Geneva, Switzerland
7. Sushi in Los Angeles, California
8. Steak in La Paz, Bolivia
9. Gyros in Sydney Australia

## Limitations
**_Coding ongoing_**