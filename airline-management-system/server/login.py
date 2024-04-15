from flask import Flask, Blueprint, jsonify ,request
from flask_cors import CORS
from datetime import datetime
from dbconnection import get_mongo_collections



# Get MongoDB collections using the connection module
collections = get_mongo_collections()
accounts_collection = collections['accounts']
users_collection = collections['users']

# Create a Blueprint object
login_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

# Define a route within the blueprint
@login_blueprint.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()
    username = data.get('user')
    password = data.get('pwd')

    # Query MongoDB to find user by username and password
    user = accounts_collection.find_one({'username': username, 'password': password})

    # Check user credentials and return response
    if user:
        # Authentication successful
        response = jsonify(message='Login successful', username=username)
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 200
    else:
        response = jsonify(message='Invalid username or password')
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 401

# Define additional routes or functions here if needed
@login_blueprint.route('/register', methods=['POST'])

def register_route():
    data = request.get_json()
    username = data.get('user')
    password = data.get('pwd')
    email = data.get('user')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone_number = data.get('phone_number')
    address = data.get('address')
    role = data.get('role')


    existing_user  = accounts_collection.find_one({'username': username})
    if existing_user:
        return jsonify(message='User already exists'), 400  # Bad request
    
   
    else:
         # Generate user ID (can use ObjectId or custom logic)
        user_id = str(accounts_collection.count_documents({}) + 1)  # Simple increment for demo
    # Create user document
        user_doc = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number,
        'address': address,
        'role': role,
        'user_id': user_id,
        'created_at': datetime.now()
    }
    # Insert new user into MongoDB
        users_collection.insert_one(user_doc)
    # Insert new user into MongoDB
        new_user = {'username': username, 'password': password,'user_id': user_id}
        accounts_collection.insert_one(new_user)
        return jsonify(message='User registered successfully'), 201

