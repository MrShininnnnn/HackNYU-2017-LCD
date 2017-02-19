from flask import Flask, render_template, redirect, url_for
from flask.ext.cache import Cache
import time
import random
import os



app = Flask(__name__)
mycache = Cache()
mycache.init_app(app)

app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)

scans = os.listdir("static/images/cancer_imgs/")

@app.route("/")
@app.cache.cached(timeout=50)
@mycache.cached()

def main():
	return render_template("index.html")

@app.route("/loading.html")
def loading():
	return render_template("loading.html")
	# time.sleep(3)
	# return render_template("index.html")

@app.route("/result1.html")
def about():
	time.sleep(5)
	scan_path = "images/cancer_imgs/" + random.choice(scans)
	prob = random.uniform(0.4,0.95) * 100
	return render_template("result1.html", prob = prob, path = scan_path)

if __name__ == '__main__':
	app.run(port=5000, debug=True, host='0.0.0.0', threaded=True)