from flask import (
    render_template, flash, request, url_for, redirect)
from holidaymanager import app, db
from holidaymanager.models import Users, Caravans, Events
from holidaymanager.models import Caravan_Bookings, Event_Bookings
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = Users(
            first_name=request.form.get("first_name"),
            last_name=request.form.get("last_name"),
            username=request.form.get("username"),
            email=request.form.get("email"),
            password=generate_password_hash(request.form.get("password")),
            admin_user=bool(
                True if request.form.get("admin_user") else False)
        )
        db.session.add(user)
        db.session.commit()
        flash("Account Registered. You can now login")
        return redirect(url_for("login.html"))
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


@app.route("/add-caravan")
def add_caravan():
    return render_template("add-caravan.html")


@app.route("/edit-caravan")
def edit_caravan():
    return render_template("edit-caravan.html")


@app.route("/add-event")
def add_event():
    return render_template("add-event.html")


@app.route("/edit-event")
def edit_event():
    return render_template("edit-event.html")
