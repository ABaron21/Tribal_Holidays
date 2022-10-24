from flask import render_template
from holidaymanager import app, db
from holidaymanager.models import Users, Caravans, Events, Bookings


@app.route("/")
def home():
    return render_template("home.html")