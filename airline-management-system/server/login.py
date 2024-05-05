from flask import Blueprint, jsonify, request
from dbconnection import get_mongo_collections
from user_operations import Register, Login

collections = get_mongo_collections()

# Create a Blueprint object named 'login_blueprint' with the URL prefix '/auth'
login_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

class Users:
    def __init__(self):
        self.accounts_collection = collections['accounts']
        self.users_collection = collections['users']

# Define the route for login within the login blueprint
@login_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    users_instance = Users()
    login_instance = Login(users_instance)
    
    success, user = login_instance.handle_login(username, password)
    if success:
        response = jsonify(message='Login successful', username=username)
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 200

    else:
        response = jsonify(message='Invalid username or password')
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 401

@login_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('userPassword')
    email = data.get('email')
    first_name = data.get('firstname')
    last_name = data.get('lastname')
    phone_number = data.get('phoneNo')
    address = data.get('address')
    
    users_instance = Users()
    register_instance = Register(users_instance)
    
    success, message = register_instance.register_user(username, password, email, first_name, last_name, phone_number, address)

    if success:
        response = jsonify(message=message, username=username)
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 201
    else:
        response = jsonify(message=message)
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 400
# Export the blueprint for use in the Flask app
