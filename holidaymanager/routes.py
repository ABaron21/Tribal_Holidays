from flask import (
    render_template, flash, session,
    request, url_for, redirect)
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
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = list(Users.query.all())
        for user in users:
            if request.form.get("username") == user.username:
                existing_user = user

        if existing_user:
            if check_password_hash(
                    existing_user.password, request.form.get("password")):
                if existing_user.admin_user:
                    session["user"] = "admin"
                else:
                    session["user"] = request.form.get("username").lower()
                flash("Welcome back, {0}".format(request.form.get("username")))
                return render_template("home.html")
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for('login'))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for('login'))


@app.route("/caravans")
def caravans():
    caravans = list(Caravans.query.order_by(Caravans.id).all())
    return render_template("caravans.html", caravans=caravans)


@app.route("/events")
def events():
    events = list(Events.query.order_by(Events.id).all())
    return render_template("events.html", events=events)


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


@app.route("/add-caravan", methods=["GET", "POST"])
def add_caravan():
    if request.method == "POST":
        caravan = Caravans(
            name=request.form.get("caravan_name"),
            img_url=request.form.get("img_url"),
            bedrooms=request.form.get("num_bedrooms"),
            additional_feature=request.form.get("additional_features"),
            available=True if request.form.get("caravan_available") else False
        )
        db.session.add(caravan)
        db.session.commit()
        flash("Caravan Added Successfully")
        return redirect(url_for('add_caravan'))
    return render_template("add-caravan.html")


@app.route("/edit-caravan")
def edit_caravan():
    return render_template("edit-caravan.html")


@app.route("/add-event", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        event = Events(
            name=request.form.get("event_name"),
            img_url=request.form.get("img_url"),
            event_date=request.form.get("event_date"),
            places_left=request.form.get("places_available")
        )
        db.session.add(event)
        db.session.commit()
        flash("Event Added Successfully")
        return redirect(url_for('add_event'))
    return render_template("add-event.html")


@app.route("/edit-event")
def edit_event():
    return render_template("edit-event.html")
