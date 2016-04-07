from flask import Flask, render_template,url_for
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/login')
def login():
	return render_template("log_in.html")

@app.route('/profile')
def profile():
	return render_template("profile.html")


if __name__ == "__main__": 
	app.run() 
