from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from bson import ObjectId  # To handle MongoDB ObjectId

app = Flask(__name__)
bcrypt = Bcrypt(app)

# MongoDB connection
client = MongoClient("mongodb+srv://deekshachandru:mrgnUeRefFTwUlsF@cluster0.j7nrn.mongodb.net/user_registration?retryWrites=true&w=majority")
db = client.user_registration  # Database name
users_collection = db.users    # Collection name

# Redirect to registration page
@app.route('/')
def home():
    return redirect(url_for('register'))

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        profession = request.form['profession']
        
        # Encrypt password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Prepare user data
        user_data = {
            'name': name,
            'password': hashed_password,
            'email': email,
            'phone': phone,
            'profession': profession
        }
        
        # Insert into MongoDB
        users_collection.insert_one(user_data)
        
        # Send success response
        return jsonify({"message": "User registered successfully!"})

    # If GET request, show the registration page
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Find the user in the database
        user = users_collection.find_one({'email': email})

        # If user exists, check the password
        if user and bcrypt.check_password_hash(user['password'], password):
            # Password matches, successful login
            return jsonify({"success": True})
        else:
            # Either user doesn't exist or password is incorrect
            return jsonify({"success": False, "message": "Invalid email or password."})

    # If GET request, show the login page
    return render_template('login.html')

# Home page route (after successful login)
@app.route('/home')
def home_page():
    return render_template('home.html')

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {'password': 0}))  # Exclude passwords from response
    # Convert ObjectId to string for JSON serialization
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify({"users": users})

# Endpoint to delete a user
@app.route('/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted successfully!"})
    else:
        return jsonify({"message": "User not found."}), 404

# Endpoint to edit a user
@app.route('/edit/<user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    # Find the user in MongoDB
    user = users_collection.find_one({"_id": ObjectId(user_id)})

    if request.method == 'POST':
        # Update user details based on form data
        updated_data = {
            "name": request.form['name'],
            "email": request.form['email'],
            "phone": request.form['phone'],
            "profession": request.form['profession']
        }
        users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": updated_data})
        return redirect(url_for('home_page'))  # Redirect to home page after editing

    # If GET request, render edit form with current user details
    if user:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string for HTML rendering
        return render_template('edit.html', user=user)
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
