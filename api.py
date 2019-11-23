from flask import Flask, request, render_template
from flask_cors import CORS
from flask import jsonify
import sys
app = Flask(__name__)
CORS(app)
tpe = {
    "id": 0,
    "city_name": "Taipei",
    "country_name": "Taiwan",
    "is_capital": True,
    "location": {
        "longitude": 121.569649,
        "latitude": 25.036786
    }
}
nyc = {
    "id": 1,
    "city_name": "New York",
    "country_name": "United States",
    "is_capital": False,
    "location": {
        "longitude": -74.004364,
        "latitude": 40.710405
    }
}
ldn = {
    "id": 2,
    "city_name": "London",
    "country_name": "United Kingdom",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}
cities = [tpe, nyc, ldn]

@app.route("/api", methods=["GET"])
def api():

    query = request.args.get("query")
    print (query)
    print ("int")


    return jsonify(cities)


if __name__ == '__main__':
    app.debug = True
    app.run()
