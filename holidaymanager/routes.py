from flask import render_template
from holidaymanager import app, db
from holidaymanager.models import Users, Caravans, Events
from holidaymanager.models import Caravan_Bookings, Event_Bookings


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


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/change-password")
def change_password():
    return render_template("change-password.html")


@app.route("/change-details")
def change_details():
    return render_template("change-details.html")


@app.route("/admin-dashboard")
def admin_dashboard():
    return render_template("admin-dashboard.html")
