from flask import Flask, request, render_template
from sklearn.externals import joblib
from flask_cors import CORS
import numpy as np

from flask import jsonify
import sys
app = Flask(__name__)
CORS(app)
safe = np.load('safe.npy')
warn = np.load('warn.npy')


# print(safe)
load = joblib.load("Heyman.joblib")
print(load.predict(safe)[0])

@app.route("/api", methods=["GET"])
def api():

    query = request.args.get("query")
    print (query)
    print ("int")

    return jsonify(load.predict(safe)[0])


if __name__ == '__main__':
    app.debug = True
    app.run()
