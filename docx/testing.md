# Testing
## User Stories
US = User story (e.g US One = user story one)
### US One
1. Open the side navbar and locate the register button.
2. (Larger Screens) Locate the register button on the right side of the navbar.
3. Fill out the form with your name, a username, your email and a password then submit.

![user-story-one](images/user-stories/us-one.PNG)

### US Two
1. Open the side navbar and locate the log in button.
2. (Larger Screens) Locate the log in button on the right side of the navbar.
3. Enter your accounts username and your password for the account.
4. If the details are correct you'll be logged in redirected to the home page, if not you'll be alerted that the username or password is wrong.

![user-story-two](images/user-stories/us-two.PNG)

### US Three
1. Open the side navbar and locate the caravans button.
2. (Larger Screens) Locate the caravans button on the right side of the navbar.
3. Scroll through all the caravans or search for caravans with a specific number of bedrooms or caravans with certain features.

![user-story-three](images/user-stories/us-three.PNG)

### US Four
1. Open the side navbar and locate the events button.
2. (Larger Screens) Locate the events button on the right side of the navbar.
3. Scroll through all the events or search for events with a certains number of spaces available or events happening on a specific date.

![user-story-four](images/user-stories/us-four.PNG)

### US Five
1. Open the side navbar and locate the profile button.
2. (Larger Screens) Locate the profile button on the right side of the navbar.
3. Scroll down the page to see your profile details, caravan bookings and event bookings.

![user-story-five](images/user-stories/us-five.PNG)

### US Six
1. Open the side navbar and locate the dashboard button.
2. (Larger Screens) Locate the dashboard button on the right side of the navbar.
3. Scroll down the page to see options for caravans and events such as adding/editing and deleting, as well viewing bookings that have been placed

![user-story-six](images/user-stories/us-six.PNG)

----
## Defensiveness
### Attempting book without being logged in
![defensive-one](images/defensiveness/defensiveness-one.PNG)

### Attempting to view the admin dashboard without being an admin user
![defensive-two](images/defensiveness/defensiveness-two.PNG)

### Attempting to view another users profile
![defensive-three](images/defensiveness/defensiveness-three.PNG)

----
## User Interaction
### User Registration
![user-registering](images/user-interaction/user-registering.PNG)
![user-registered](images/user-interaction/user-registered.PNG)
![user-registered-db](images/user-interaction/user-registered-db.PNG)

----
### User Logging In
![user-logging-in](images/user-interaction/user-logging-in.PNG)
![user-logged-in](images/user-interaction/user-logged-in.PNG)

----
### Caravan Searching
![caravan-searching](images/user-interaction/caravan-searching.PNG)
![caravan-searched](images/user-interaction/caravan-searched.PNG)

----
### Event Searching
![event-searching](images/user-interaction/event-searching.PNG)
![event-searched](images/user-interaction/event-searched.PNG)

----
### Caravan Booking
![caravan-booking](images/user-interaction/caravan-booking.PNG)
![caravan-booked](images/user-interaction/caravan-booked.PNG)
![caravan-booked-db](images/user-interaction/caravan-booked-db.PNG)

----
### Event Booking
![event-booking](images/user-interaction/event-booking.PNG)
![event-booked](images/user-interaction/event-booked.PNG)
![event-booked-db](images/user-interaction/event-booked-db.PNG)

----
### Changing Account Details
![changing-details](images/user-interaction/changing-details.PNG)
![changed-details](images/user-interaction/changed-details.PNG)

----
### Deleting Account
![deleting-account](images/user-interaction/deleting-account.PNG)
![deleted-account](images/user-interaction/deleted-account.PNG)
![deleted-account-db](images/user-interaction/deleted-account-db.PNG)

----
## Code Validation
### HTML

### CSS

----
## Bugs
### Profile Page Bug
![profile-bug](images/bugs/profile-page-bug.PNG)

As shown above when the development test user tried to view their profile it would show the profile page for the 'Test One' user, the reason for this bug is that when retrieving a user's profile it does it based on the username given which has been stored as a session cookie when the user logged in.

To resolve this bug what was changed was that within the user session cookie it would store the users ID number instead of their username so this would allow for the user to be able to see their profile and only their profile, also with this change it allowed for the defensiveness to be put into place for the profile page.