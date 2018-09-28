from geocode import getGeocodeLocation
import json
import httplib2
import sys
import codecs


reload(sys)
sys.setdefaultencoding('utf8')
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

    # Make an API request for Search
    h = httplib2.Http()
    response, content = h.request(url,'GET')

    # Process the response
    result = json.loads(content)

    # Check if no venue found
    if not result['response']['venues']:
        return 'No restaurants found'

	# Grab the first restaurant
    restaurant_name = result['response']['venues'][0]['name']
    restaurant_address = (' ').join(result['response']['venues'][0]
                                    ['location']['formattedAddress'])

    print('\nRestaurant Name: ' + restaurant_name)
    print('Restaurant Address: ' + restaurant_address)

    # Make an API request for Venue photo
    venue_id = result['response']['venues'][0]['id']

    url = ('https://api.foursquare.com/v2/venues/%s/photos?'
           'client_id=%s&'
           'client_secret=%s&'
           'v=20130815&'
           'limit=1' % (venue_id, foursquare_client_id, foursquare_client_secret))
    response, content = h.request(url,'GET')
    result = json.loads(content)

    # Get a  300x300 picture of the restaurant using the venue_id
	# If no image is available, insert default a image url
    if result['response']['photos']['count'] != 1:
        image = ('https://cdn.pixabay.com/photo/2016/03/05/19/02/'
                 'hamburger-1238246_960_720.jpg')
    else:
        image = (result['response']['photos']['items'][0]['prefix'] +
                 '300x300' +
                 result['response']['photos']['items'][0]['suffix'])
    print('Image: ' + image)

    # Return a dictionary of name, address and image
    return {'name':restaurant_name,
            'address':restaurant_address,
            'image':image}


if __name__ == '__main__':
    findARestaurant('Pizza', 'Tokyo, Japan')
    findARestaurant('Tacos', 'Jakarta, Indonesia')
    findARestaurant('Tapas', 'Maputo, Mozambique')
    findARestaurant('Falafel', 'Cairo, Egypt')
    findARestaurant('Spaghetti', 'New Delhi, India')
    findARestaurant('Cappuccino', 'Geneva, Switzerland')
    findARestaurant('Sushi', 'Los Angeles, California')
    findARestaurant('Steak', 'La Paz, Bolivia')
    findARestaurant('Gyros', 'Sydney Australia')