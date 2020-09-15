from flask import Flask, redirect, request, render_template, url_for
import flask_monitoringdashboard as dashboard
from random import shuffle
import os

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

@app.route("/submit", methods=["POST"])
def submit():
	#os.makedirs("feedback", exist_ok=True)
	data = request.form["link"]

	with open("feedback.txt", "a") as f:
		f.write(data+"\n")

	return redirect(url_for("index"))


PORT = 8000

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=PORT)
