User Registration and Management System
This project is a web application built with Flask, MongoDB, and Bootstrap that enables users to register, log in, view, edit, and delete user profiles. This system includes password hashing for security and provides a simple dashboard for user management.
Table of Contents
Features
Technologies Used
Setup and Installation
Project Structure
Usage
API Endpoints
Technical Overview
License

Features
User Registration: New users can register with their name, email, phone number, and profession. Passwords are securely stored using hashing.
User Login: Registered users can log in with their email and password.
User Management Dashboard:
View all registered users (admin functionality).
Edit user information.
Delete user accounts.
Technologies Used
Backend: Flask, MongoDB Atlas
Frontend: HTML, Bootstrap, jQuery
Security: Password hashing with Flask-Bcrypt
Setup and Installation
Prerequisites
Python 3.x: Ensure Python is installed.
MongoDB Atlas: Sign up and create a cluster on MongoDB Atlas.
Git: To clone the repository.
Steps
Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name


Set Up a Virtual Environment:
bash
Copy code
python -m venv venv


Activate the Virtual Environment:
Windows:
bash
Copy code
.\venv\Scripts\activate


macOS/Linux:
bash
Copy code
source venv/bin/activate


Install Dependencies:
bash
Copy code
pip install Flask pymongo Flask-Bcrypt


Configure MongoDB Atlas:
Sign up and create a cluster in MongoDB Atlas.
Create a database user and whitelist your IP.
Replace the MongoDB URI in app.py with your cluster's connection string.
Run the Application:
bash
Copy code
python app.py


Access the Application:
Open your browser and navigate to http://127.0.0.1:5000/.
Project Structure
bash
Copy code
.
├── app.py                  # Main application file
├── README.md               # Project documentation
├── requirements.txt        # List of dependencies
└── templates               # HTML templates
    ├── register.html       # Registration page
    ├── login.html          # Login page
    ├── home.html           # Home/dashboard page
    └── edit.html           # Edit user details page

Usage
Register a New User:
Navigate to /register.
Fill in the registration form and submit.
Log in:
Go to /login.
Enter the registered email and password to access the dashboard.
View All Users:
After logging in, access the /home page to see a list of all users.
Edit User Information:
On the /home page, click the "Edit" button next to a user to modify their information.
Delete a User:
Click the "Delete" button next to a user to remove them from the database.
API Endpoints
Method
Endpoint
Description
GET
/register
Renders the registration page
POST
/register
Handles user registration
GET
/login
Renders the login page
POST
/login
Authenticates the user
GET
/home
Displays the user dashboard
GET
/users
Fetches all registered users
DELETE
/delete/<user_id>
Deletes the user with the specified user_id
GET
/edit/<user_id>
Renders edit page with user’s current details
POST
/edit/<user_id>
Updates the user’s information in the database

Technical Overview
Flask
Routing: Manages all HTTP requests (e.g., register, login, home).
Backend Logic: Implements registration, login, user fetching, editing, and deletion.
MongoDB Atlas
Database: Stores user data in the user_registration database within a users collection.
NoSQL Structure: Each user is a document with fields for name, email, phone, profession, and password.
Flask-Bcrypt
Password Security: Passwords are hashed using Bcrypt before storage, protecting user credentials.
Frontend
HTML, Bootstrap: Provides a clean and responsive user interface.
jQuery: Enables AJAX for smooth and responsive page updates without full reloads.
Security
Password Hashing: Passwords are stored securely using hashing, ensuring data safety even if database access is compromised.
Client-Server Validation: Forms are validated on the client side for basic checks, and on the server side for security.
License
This project is open-source and available under the MIT License.

