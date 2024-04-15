from flask import Flask
from flask_cors import CORS
from login import login_blueprint  # Import the blueprint object from login.py
from dbconnection import get_mongo_collections

# Create a Flask app instance
app = Flask(__name__)
# Enable CORS for all origins on all routes
CORS(app,supports_credentials=True)

# Register the login blueprint with the Flask app
app.register_blueprint(login_blueprint)

# Define a function in server.py to call a function from login.py
def call_login_function():
    # This function can be used to invoke any function defined within login.py
    with app.test_request_context():
        response = login_blueprint.login_route()
        return response



# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
