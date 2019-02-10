from flask import Flask, Response, render_template
from distancesensor import get_distance
import json


app = Flask(__name__)

def sensor():
	return json.dumps(get_distance())

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/dormbell')
def dormbell():
	return Response(sensor(), mimetype="application/json")

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 80, debug=True, threaded=True)
