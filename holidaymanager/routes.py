from flask import (
    render_template, flash, session,
    request, url_for, redirect)
from holidaymanager import app, db
from holidaymanager.models import Users, Caravans, Events
from holidaymanager.models import Caravan_Bookings, Event_Bookings
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    caravans = list(Caravans.query.order_by(Caravans.id).all())
    events = list(Events.query.order_by(Events.id).all())
    return render_template(
        "home.html", caravans=caravans, events=events)


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
                    return redirect(url_for('home'))
                else:
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back, {0}".format(
                        request.form.get("username")))
                    return redirect(url_for('home'))
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


@app.route("/caravans", methods=["GET", "POST"])
def caravans():
    caravans = list(Caravans.query.order_by(Caravans.id).all())
    if request.method == "POST":
        select = request.form.get("select_filter")
        if select == "bedrooms":
            search = request.form.get("search")
            return redirect(
                url_for('caravan_search_bedrooms', num_bedrooms=search))
        elif select == "features":
            search = request.form.get("search")
            return redirect(
                url_for('caravan_search_features', feature=search))
    return render_template("caravans.html", caravans=caravans)


@app.route("/caravan-search-bedrooms/<int:num_bedrooms>")
def caravan_search_bedrooms(num_bedrooms):
    caravans = list(Caravans.query.order_by(Caravans.id).all())
    return render_template(
        "caravan-search-bedrooms.html",
        caravans=caravans, num_bedrooms=num_bedrooms)


@app.route("/caravan-search-features/<feature>")
def caravan_search_features(feature):
    caravans = list(Caravans.query.order_by(Caravans.id).all())
    print(feature)
    return render_template(
        "caravan-search-features.html",
        caravans=caravans, feature=feature)


@app.route("/caravan-booking/<int:caravan_id>", methods=["GET", "POST"])
def caravan_booking(caravan_id):
    caravan = Caravans.query.get_or_404(caravan_id)
    customers = list(Users.query.order_by(Users.username).all())
    for customer in customers:
        if session['user'] == customer.username:
            customer = customer
    if request.method == "POST":
        customer_name = request.form.get('first_name')
        customer_name += request.form.get('last_name')
        booking = Caravan_Bookings(
            customer=customer_name,
            user_id=customer.id,
            caravan_name=caravan.name,
            caravan_id=caravan.id,
            start_date=request.form.get('start_date'),
            end_date=request.form.get('end_date')
        )
        caravan.available = False
        db.session.add(booking)
        db.session.commit()
        flash("Caravan has been successfully booked")
        return redirect(url_for("home"))
    return render_template("caravan-booking.html", caravan=caravan)


@app.route("/remove-caravan-booking/<int:c_booking_id>")
def remove_caravan_booking(c_booking_id):
    c_booking = Caravan_Bookings.query.get_or_404(c_booking_id)
    db.session.delete(booking)
    db.session.commit()
    flash("Booking has been cancelled")
    return redirect(url_for('profile', username=session['user']))


@app.route("/events", methods=["GET", "POST"])
def events():
    events = list(Events.query.order_by(Events.id).all())
    if request.method == "POST":
        select = request.form.get("select_filter")
        if select == "spaces":
            search = request.form.get("search")
            return redirect(
                url_for('events_search_spaces', num_spaces=search))
        elif select == "date":
            search = request.form.get("search")
            return redirect(
                url_for('events_search_date', date=search))
    return render_template("events.html", events=events)


@app.route("/events-search-spaces/<int:num_spaces>", methods=["GET", "POST"])
def events_search_spaces(num_spaces):
    events = list(Events.query.order_by(Events.id).all())
    return render_template(
        "events-search-spaces.html", events=events, num_spaces=num_spaces)


@app.route("/events-search-date/<date>", methods=["GET", "POST"])
def events_search_date(date):
    events = list(Events.query.order_by(Events.id).all())
    return render_template(
        "events-search-date.html", events=events, date=date)


@app.route("/event-booking/<int:event_id>", methods=["GET", "POST"])
def event_booking(event_id):
    event = Events.query.get_or_404(event_id)
    customers = list(Users.query.order_by(Users.username).all())
    for customer in customers:
        if session['user'] == customer.username:
            customer = customer
    if request.method == "POST":
        customer_name = request.form.get('first_name').lower()
        customer_name += " "
        customer_name += request.form.get('last_name').lower()
        booking = Event_Bookings(
            user_id=customer.id,
            customer=customer_name,
            event_id=event.id,
            event_name=event.name,
            event_img=event.img_url,
            event_date=event.event_date,
            places_booked=int(request.form.get('spots_wanted'))
        )
        spots_left = int(
            event.places_left) - int(request.form.get('spots_wanted'))
        event.places_left = spots_left
        db.session.add(booking)
        db.session.commit()
        flash("Event has been successfully booked")
        return redirect(url_for("home"))
    return render_template("event-booking.html", event=event)


@app.route("/remove-event-booking/<int:e_booking_id>")
def remove_event_booking(e_booking_id):
    e_booking = Event_Bookings.query.get_or_404(e_booking_id)
    db.session.delete(e_booking)
    db.session.commit()
    flash("Booking has been cancelled")
    return redirect(url_for('home'))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    accounts = list(Users.query.order_by(Users.username).all())
    for account in accounts:
        if username == account.username:
            account = account
    c_bookings = list(Caravan_Bookings.query.all())
    e_bookings = list(
        Event_Bookings.query.all())

    return render_template(
        "profile.html", account=account,
        c_bookings=c_bookings, e_bookings=e_bookings)


@app.route("/change-password/<int:user_id>", methods=["GET", "POST"])
def change_password(user_id):
    user = Users.query.get_or_404(user_id)

    if request.method == "POST":
        if check_password_hash(
                user.password, request.form.get("old_password")):
            if request.form.get("new") == request.form.get("confirm"):
                user.password = generate_password_hash(
                    request.form.get("new"))
                db.session.commit()
                flash("Password Changed Successfully")
                return redirect(url_for('profile', username=session['user']))
            else:
                flash("New & Confirm Password didn't match")
                return redirect(url_for('change_password', user_id=user.id))
        else:
            flash("Couldn't Recognise Your Old Password")
            return redirect(url_for('change_password', user_id=user.id))

    return render_template("change-password.html", user=user)


@app.route("/change-details/<int:user_id>", methods=["GET", "POST"])
def change_details(user_id):
    user = Users.query.get_or_404(user_id)

    if request.method == "POST":
        user.first_name = request.form.get("first_name")
        user.last_name = request.form.get("last_name")
        user.username = request.form.get("username")
        user.email = request.form.get("email")
        db.session.commit()
        flash("Account details updated successfully")
        session['user'] = request.form.get("username")
        return redirect(url_for('profile', username=session['user']))
    return render_template("change-details.html", user=user)


@app.route("/admin-dashboard")
def admin_dashboard():
    caravan_bookings = list(Caravan_Bookings.query.all())
    event_bookings = list(Event_Bookings.query.all())
    return render_template(
        "admin-dashboard.html", caravan_bookings=caravan_bookings,
        event_bookings=event_bookings)


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


@app.route("/edit-caravan-search", methods=["GET", "POST"])
def edit_caravan_search():
    caravans = list(Caravans.query.order_by(Caravans.id).all())
    if request.method == "POST":
        name = request.form.get("search")
        return redirect(url_for('edit_caravan_searched', caravan_name=name))
    return render_template("edit-caravan-search.html", caravans=caravans)


@app.route("/edit-caravan-searched/<caravan_name>", methods=["GET", "POST"])
def edit_caravan_searched(caravan_name):
    caravans = list(Caravans.query.order_by(Caravans.id).all())
    return render_template(
        "edit-caravan-searched.html",
        caravans=caravans, caravan_name=caravan_name)


@app.route("/edit-caravan/<int:caravan_id>", methods=["GET", "POST"])
def edit_caravan(caravan_id):
    caravan = Caravans.query.get_or_404(caravan_id)

    if request.method == "POST":
        caravan.name = request.form.get("caravan_name")
        caravan.img_url = request.form.get("img_url")
        caravan.bedrooms = request.form.get("num_bedrooms")
        caravan.additional_feature = request.form.get("additional_features")
        caravan.available = True if request.form.get(
            "caravan_available") else False

        db.session.commit()
        flash("Caravan Edited Successfully")
        return redirect(url_for('edit_caravan_search'))

    return render_template("edit-caravan.html", caravan=caravan)


@app.route("/delete-caravan")
def delete_caravan():
    caravans = list(Caravans.query.order_by(Caravans.id).all())
    return render_template("delete-caravan.html", caravans=caravans)


@app.route("/remove-caravan/<int:caravan_id>")
def remove_caravan(caravan_id):
    caravan = Caravans.query.get_or_404(caravan_id)
    db.session.delete(caravan)
    db.session.commit()
    flash("Caravan has been deleted")
    return redirect(url_for('delete_caravan'))


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


@app.route("/edit-event-search", methods=["GET", "POST"])
def edit_event_search():
    events = list(Events.query.order_by(Events.id).all())
    if request.method == "POST":
        name = request.form.get("search")
        return redirect(url_for('edit_event_searched', event_name=name))
    return render_template("edit-event-search.html", events=events)


@app.route("/edit-event-searched/<event_name>", methods=["GET", "POST"])
def edit_event_searched(event_name):
    events = list(Events.query.order_by(Events.id).all())
    return render_template(
        "edit-event-searched.html", events=events, event_name=event_name)


@app.route("/edit-event/<int:event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    event = Events.query.get_or_404(event_id)

    if request.method == "POST":
        event.name = request.form.get("event_name"),
        event.img_url = request.form.get("img_url"),
        event.event_date = request.form.get("event_date"),
        event.places_left = request.form.get("places_available")
        db.session.commit()
        flash("Event Edited Successfully")
        return redirect(url_for('edit_event_search'))

    return render_template("edit-event.html", event=event)


@app.route("/delete-event")
def delete_event():
    events = list(Events.query.order_by(Events.id).all())
    return render_template("delete-event.html", events=events)


@app.route("/remove-event/<int:event_id>")
def remove_event(event_id):
    event = Events.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    flash("Event has been deleted")
    return redirect(url_for('delete_event'))
