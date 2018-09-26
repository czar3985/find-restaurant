import httplib2
import json

def getGeocodeLocation(locationInput):
    """Determine the latitude and longitude based on the indicated location"""

    # Keep the key secret
    key = json.loads(open('client_secrets.json', 'r').
                     read())['google']['api_key']

    # There should be no breaks in the URL path
    address = locationInput.replace(" ","+")

    # Build the url using the parameters needed by the API
    url = ('https://maps.googleapis.com/maps/api/geocode/json?'
           'address=%s&key=%s'% (address, key))

    # Make an API request
    h = httplib2.Http()
    response, content = h.request(url,'GET')

    # Process the response
    result = json.loads(content)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']

    return (latitude, longitude)
