from holidaymanager import db


class Users(db.Model):
    # schema for Users model
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    last_name = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=True, nullable=False)
    caravan_booking = db.relationship(
        "Caravan_Bookings", backref="users", cascade="all, delete", lazy=True
    )
    event_booking = db.relationship(
        "Event_Bookings", backref="users", cascade="all, delete", lazy=True
    )
    admin_user = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return "Name: {0} | Email: {1} | Created: {2}".format(
            self.name, self.email, self.user_created
        )


class Caravans(db.Model):
    # schema for Caravans model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    additional_feature = db.Column(db.String(50), nullable=False)
    available = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return "Name: {0} | Bedrooms: {1} | Available: {2}".format(
            self.name, self.bedrooms, self.available
        )


class Events(db.Model):
    # schema for Events model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    places_left = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "Name: {0} | Date: {1} | Spaces Available: {2}".format(
            self.name, self.event_date, self.places_left
        )


class Caravan_Bookings(db.Model):
    # schema for Bookings model
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    customer = db.Column(db.String(50), nullable=False)
    caravan_id = db.Column(
        db.Integer, db.ForeignKey("caravans.id"), nullable=False)
    caravan_name = db.Column(db.String(50), nullable=False)
    caravan_img = db.Column(db.String(250), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return "Customer Name: {0} | Caravan: {1} | Booked: {2}-{3}".format(
            self.customer, self.caravan_name, self.start_date, self.end_date
        )


class Event_Bookings(db.Model):
    # schema for Bookings model
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    customer = db.Column(db.String(50), nullable=False)
    event_id = db.Column(
        db.Integer, db.ForeignKey("events.id"), nullable=False)
    event_name = db.Column(db.String(50), nullable=False)
    event_img = db.Column(db.String(250), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    places_booked = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "Customer: {0} | Event: {1} | Date: {2} | Places: {3}".format(
            self.customer, self.event_name, self.event_date, self.places_booked
        )
