from findARestaurant import findARestaurant
from flask import Flask, jsonify, request
import sys
import codecs


sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

app = Flask(__name__)


@app.route('/restaurant')
def all_restaurants_handler():
    location = request.args.get('location', '')
    mealtype = request.args.get('mealtype', '')

    restaurantInfo = findARestaurant(mealtype, location)

    return jsonify(Restaurant=[restaurantInfo])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)



