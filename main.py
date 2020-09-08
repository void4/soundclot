from flask import Flask, redirect, request, render_template
import flask_monitoringdashboard as dashboard
from random import shuffle

app = Flask(__name__)

dashboard.config.init_from(file="config.cfg")
dashboard.bind(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
	with open("videos.txt") as f:
		videos = f.read().splitlines()
	shuffle(videos)	
	return render_template("index.html", videos=videos)

PORT = 8000

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=PORT)
