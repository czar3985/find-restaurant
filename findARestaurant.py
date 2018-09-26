from geocode import getGeocodeLocation
import json
import httplib2
import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = json.loads(open('client_secrets.json', 'r').
                                  read())['foursquare']['client_id']
foursquare_client_secret = json.loads(open('client_secrets.json', 'r').
                                      read())['foursquare']['client_secret']


def findARestaurant(mealType,location):
	# Get the latitude and longitude coordinates of the location string
    latitude, longitude = getGeocodeLocation(location)

	# Use foursquare API to find a nearby restaurant with the latitude,
	# longitude, and mealType strings
	# Build the URL using this format:
	# https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&
	# client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    url = ('https://api.foursquare.com/v2/venues/search?'
           'client_id=%s&'
           'client_secret=%s&'
           'v=20130815&'
           'll=%s,%s&'
           'query=%s'% (foursquare_client_id, foursquare_client_secret,
                        latitude, longitude, mealType))

    # Make an API request
    h = httplib2.Http()
    response, content = h.request(url,'GET')

    # Process the response
    result = json.loads(content)

	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url

    return result


if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
    findARestaurant("Gyros", "Sydney Australia")