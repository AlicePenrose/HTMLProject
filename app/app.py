from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about_us")
def about_us():
    return render_template("aboutus.html")

@app.route("/contacts")
def contact():
    return render_template("contact.html")