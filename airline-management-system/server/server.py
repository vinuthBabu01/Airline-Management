from flask import Flask, request, jsonify
from flask_cors import CORS
from login import Users, login_blueprint  # Import the Users class and login_blueprint from login.py
from dbconnection import get_mongo_collections

# Create a Flask app instance
app = Flask(__name__)
# Enable CORS for all origins on all routes
CORS(app, supports_credentials=True)

# Initialize Users service
users_service = Users()  # Assuming 'Users' is a valid class representing a service

# Define route within the login blueprint
@login_blueprint.route('/auth', methods=['POST'])
def handle_auth_request():
    data = request.get_json()
    action = data.get('action')

    response = users_service.handle_request(data)
    return response

# Register the login blueprint with the Flask app
app.register_blueprint(login_blueprint, url_prefix='/auth')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)




# # Get MongoDB collections using the connection module
# collections = get_mongo_collections()
# accounts_collection = collections['accounts']
# users_collection = collections['users']

# # # Create a Blueprint object
# login_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

# # Define a route within the blueprint
# @login_blueprint.route('/login', methods=['POST'])
# def login_route():
#     data = request.get_json()
#     username = data.get('user')
#     password = data.get('pwd')

#     # Query MongoDB to find user by username and password
#     user = accounts_collection.find_one({'username': username, 'password': password})

#     # Check user credentials and return response
#     if user:
#         # Authentication successful
#         response = jsonify(message='Login successful', username=username)
#         response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
#         response.headers.add('Access-Control-Allow-Credentials', 'true')
#         return response, 200
#     else:
#         response = jsonify(message='Invalid username or password')
#         response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
#         response.headers.add('Access-Control-Allow-Credentials', 'true')
#         return response, 401

# # Define additional routes or functions here if needed
# @login_blueprint.route('/register', methods=['POST'])

# def register_route():
#     data = request.get_json()
#     username = data.get('user')
#     password = data.get('pwd')
#     email = data.get('user')
#     first_name = data.get('firstname')
#     last_name = data.get('lastname')
#     phone_number = data.get('phone')
#     address = data.get('address')
#     role = data.get('role')


#     existing_user  = accounts_collection.find_one({'username': username})
#     if existing_user:
#         return jsonify(message='User already exists'), 400  # Bad request
    
   
#     else:
#          # Generate user ID (can use ObjectId or custom logic)
#         user_id = str(accounts_collection.count_documents({}) + 1)  # Simple increment for demo
#     # Create user document
#         user_doc = {
#         'email': email,
#         'first_name': first_name,
#         'last_name': last_name,
#         'phone_number': phone_number,
#         'address': address,
#         'role': role,
#         'user_id': user_id,
#         'created_at': datetime.now()
#     }
#     # Insert new user into MongoDB
#         users_collection.insert_one(user_doc)
#     # Insert new user into MongoDB
#         new_user = {'username': username, 'password': password,'user_id': user_id}
#         accounts_collection.insert_one(new_user)
#         return jsonify(message='User registered successfully'), 201

