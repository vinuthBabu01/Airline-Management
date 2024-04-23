from flask import Blueprint, jsonify, request
from datetime import datetime
from dbconnection import get_mongo_collections

collections = get_mongo_collections()
accounts_collection = collections['accounts']
users_collection = collections['users']

# Create a Blueprint object named 'login_blueprint' with the URL prefix '/auth'
login_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

class Users:
    def __init__(self):
        self.accounts_collection = accounts_collection
        self.users_collection = users_collection

    def handle_request(data):
        action = data.get('action')
        if action == 'login':
            return self._authenticate_user(data)
        elif action == 'register':
            return self._register_user(data)
        else:
            return jsonify(message='Invalid action requested'), 400

    def _authenticate_user(self, data):
        username = data.get('user')
        password = data.get('pwd')
        user = self.accounts_collection.find_one({'username': username, 'password': password})

        if user:
            response = jsonify(message='Login successful', username=username)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
        else:
            response = jsonify(message='Invalid username or password')
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 401
        
    def _register_user(self, data):
        username = data.get('user')
        password = data.get('pwd')
        email = data.get('email')
        first_name = data.get('firstname')
        last_name = data.get('lastname')
        phone_number = data.get('phone')
        address = data.get('address')
        role = data.get('role')

        existing_user = self.accounts_collection.find_one({'username': username})
        if existing_user:
            response = jsonify(message='User already exists')
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 400

        user_id = str(self.accounts_collection.count_documents({}) + 1)
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
        self.users_collection.insert_one(user_doc)

        new_user = {'username': username, 'password': password, 'user_id': user_id}
        self.accounts_collection.insert_one(new_user)

        return jsonify(message='User registered successfully'), 201

# Define the route for login within the login blueprint
@login_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    action = 'login'  # Assuming this is a login action
    response = Users().handle_request(action, data)
    return response

# Export the blueprint for use in the Flask app
