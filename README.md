# Find a Restaurant

An application that finds a resturant given a location and
a query string. 

It makes API requests to Google Maps' Geolocation API and 
Foursquare's Search and Venue Photos API.

It also provides an API endpoint for other applications to use.

## Prerequisites

1. python
2. python libraries: json, httplib2, sys, codecs
3. Python scripts from this repository
4. Google developer account
5. Google API key
6. Foursquare developer account
7. Foursquare API client ID and client secret
8. `client_secrets.json` with the Google API key, Foursquare client
ID and client secret fields filled in 

#### How to get a Google API key
Refer to the guide in https://developers.google.com/maps/documentation/javascript/get-api-key
to get an API key. You may need to indicate some billing information
before you can proceed with acquiring an API key to be used for Google Maps API requests.

#### How to get a Foursquare API client ID and secret
Refer to the guide in https://developer.foursquare.com/docs/api to create 
a developer account, an app and retrieve the client ID and client secret for
Foursquare API requests.

## Usage

#### 1. Running findARestaurant.py
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

#### 2. Importing findARestaurant function
Alternatively, the function can be used by importing the function `findARestaurant`.
Pass a meal type and location as arguments.

Example:

```python
from findARestaurant import findARestaurant
findARestaurant('Pizza','Antartica')
```

#### 3. Accessing the app's API endpoint

An API endpoint is provided and can be accessed with a GET request.
The result is provided in JSON format.

> Method: GET
> 
>URL: http://localhost:5000/restaurant
> 
>Parameters:
>- location: City or Address
>- mealtype: Food item
>
>Example: http://localhost:5000/restaurant?location=Los+Angeles+California&mealtype=pasta
>