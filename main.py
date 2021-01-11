from flask import Flask, redirect, request, render_template, url_for
import flask_monitoringdashboard as dashboard
from random import choice, shuffle
import os

app = Flask(__name__)

dashboard.config.init_from(file="config.cfg")
dashboard.bind(app)

def getVideos():
	with open("videos.txt") as f:
		videos = f.read().splitlines()
	#shuffle(videos)
	return videos

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
	videos = [choice(getVideos())]
	return render_template("all.html", videos=videos)

@app.route('/all')
def allsongs():
	videos = getVideos()[::-1]
	return render_template("all.html", videos=videos)

@app.route('/dance')
def dance():
	return render_template("dance.html")

@app.route("/submit", methods=["POST"])
def submit():
	#os.makedirs("feedback", exist_ok=True)
	data = request.form["link"]

	with open("feedback.txt", "a") as f:
		f.write(data+"\n")

	return redirect(url_for("index"))


PORT = 8000

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=PORT, debug=False)
