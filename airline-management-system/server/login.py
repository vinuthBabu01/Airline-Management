from flask import Flask, Blueprint, jsonify ,request
from flask_cors import CORS
from dbconnection import get_mongo_collections



# Get MongoDB collections using the connection module
collections = get_mongo_collections()
users_collection = collections['accounts'] 

# Create a Blueprint object
login_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

# Define a route within the blueprint
@login_blueprint.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()
    username = data.get('user')
    password = data.get('pwd')

    # Query MongoDB to find user by username and password
    user = users_collection.find_one({'username': username, 'password': password})

    # Example: Check user credentials and return response
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
