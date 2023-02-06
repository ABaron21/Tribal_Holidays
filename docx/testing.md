# Testing
## User Stories
US = User story (e.g US One = user story one)
### US One
1. Open the side navbar and locate the register button.
2. (Larger Screens) Locate the register button on the right side of the navbar.
3. Fill out the form with your name, a username, your email and a password then submit.

![user-story-one](images/user-stories/us-one.png)

### US Two
1. Open the side navbar and locate the log in button.
2. (Larger Screens) Locate the log in button on the right side of the navbar.
3. Enter your accounts username and your password for the account.
4. If the details are correct you'll be logged in redirected to the home page, if not you'll be alerted that the username or password is wrong.

![user-story-two](images/user-stories/us-two.png)

### US Three
1. Open the side navbar and locate the caravans button.
2. (Larger Screens) Locate the caravans button on the right side of the navbar.
3. Scroll through all the caravans or search for caravans with a specific number of bedrooms or caravans with certain features.

![user-story-three](images/user-stories/us-three.png)

### US Four
1. Open the side navbar and locate the events button.
2. (Larger Screens) Locate the events button on the right side of the navbar.
3. Scroll through all the events or search for events with a certains number of spaces available or events happening on a specific date.

![user-story-four](images/user-stories/us-four.png)

### US Five
1. Open the side navbar and locate the profile button.
2. (Larger Screens) Locate the profile button on the right side of the navbar.
3. Scroll down the page to see your profile details, caravan bookings and event bookings.

![user-story-five](images/user-stories/us-five.png)

### US Six
1. Open the side navbar and locate the dashboard button.
2. (Larger Screens) Locate the dashboard button on the right side of the navbar.
3. Scroll down the page to see options for caravans and events such as adding/editing and deleting, as well viewing bookings that have been placed

![user-story-six](images/user-stories/us-six.png)

----
## Defensiveness
### Attempting book without being logged in
![defensive-one](images/defensiveness/defensiveness-one.png)

### Attempting to view the admin dashboard without being an admin user
![defensive-two](images/defensiveness/defensiveness-two.png)

### Attempting to view another users profile
![defensive-three](images/defensiveness/defensiveness-three.png)

----
## User Interaction
### User Registration
![user-registering](images/user-interaction/user-registering.png)
![user-registered](images/user-interaction/user-registered.png)
![user-registered-db](images/user-interaction/user-registered-db.png)

----
### User Logging In
![user-logging-in](images/user-interaction/user-logging-in.png)
![user-logged-in](images/user-interaction/user-logged-in.png)

----
### Caravan Searching
![caravan-searching](images/user-interaction/caravan-searching.png)
![caravan-searched](images/user-interaction/caravan-searched.png)

----
### Event Searching
![event-searching](images/user-interaction/event-searching.png)
![event-searched](images/user-interaction/event-searched.png)

----
### Caravan Booking
![caravan-booking](images/user-interaction/caravan-booking.png)
![caravan-booked](images/user-interaction/caravan-booked.png)
![caravan-booked-db](images/user-interaction/caravan-booked-db.png)

----
### Event Booking
![event-booking](images/user-interaction/event-booking.png)
![event-booked](images/user-interaction/event-booked.png)
![event-booked-db](images/user-interaction/event-booked-db.png)

----
### Changing Account Details
![changing-details](images/user-interaction/changing-details.png)
![changed-details](images/user-interaction/changed-details.png)

----
### Deleting Account
![deleting-account](images/user-interaction/deleting-account.png)
![deleted-account](images/user-interaction/deleted-account.png)
![deleted-account-db](images/user-interaction/deleted-account-db.png)

----
## Code Validation
### HTML
#### Home Page
![home-html-validation](images/code-validation/html-validation-home.png)

----
#### Register Page
![register-html-validation](images/code-validation/html-validation-register.png)

----
#### Login Page
![login-html-validation](images/code-validation/html-validation-login.png)

----
#### Caravans Page
![caravans-html-validation](images/code-validation/html-validation-caravans.png)

----
#### Events Page
![events-html-validation](images/code-validation/html-validation-events.png)

----
#### Caravans Searched Page
![caravans-searched-html-validation](images/code-validation/html-validation-caravans-searched.png)

----
#### Events Searched Page
![events-searched-html-validation](images/code-validation/html-validation-events-searched.png)

----
#### Caravan Booking Page
![caravan-booking-html-validation](images/code-validation/html-validation-caravan-booking.png)

----
#### Event Booking Page
![event-booking-html-validation](images/code-validation/html-validation-event-booking.png)

----
#### Admin Dashboard Page
![admin-dashboard-html-validation](images/code-validation/html-validation-admin-dashboard.png)

----
#### Profile Page
![profile-html-validation](images/code-validation/html-validation-profile.png)

----
#### Change Details Page
![change-details-html-validation](images/code-validation/html-validation-change-details.png)

----
#### Change Password Page
![change-password-html-validation](images/code-validation/html-validation-change-password.png)

----
### CSS
![css-validation](images/code-validation/css-validation.png)

----
## Bugs
### Profile Page Bug
![profile-bug](images/bugs/profile-page-bug.png)

As shown above when the development test user tried to view their profile it would show the profile page for the 'Test One' user, the reason for this bug is that when retrieving a user's profile it does it based on the username given which has been stored as a session cookie when the user logged in.

To resolve this bug what was changed was that within the user session cookie it would store the users ID number instead of their username so this would allow for the user to be able to see their profile and only their profile, also with this change it allowed for the defensiveness to be put into place for the profile page.