from flask import render_template
from holidaymanager import app, db
from holidaymanager.models import Users, Caravans, Events, Bookings


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/caravans")
def caravans():
    return render_template("caravans.html")


@app.route("/events")
def events():
    return render_template("events.html")
