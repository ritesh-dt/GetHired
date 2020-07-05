from flask import Flask
from flask import render_template, redirect, flash

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("home.jinja")

@app.route("/job")
def job():
	return render_template("job.jinja")

if __name__ == "__main__":
	app.run(debug=True)