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
    # Example: Call a function from login.py
    # For demonstration, you can call the login_route function
    # This function can be used to invoke any function defined within login.py
    with app.test_request_context():
        response = login_blueprint.login_route()
        return response


def main():
    # Get MongoDB collections using the connection module
    collections = get_mongo_collections()

# Iterate over each collection and query documents
    for collection_name, collection in collections.items():
        print(f"Documents in collection '{collection_name}':")
        cursor = collection.find({})  # Retrieve all documents (you can specify a query here)
        for document in cursor:
            print(document)
        print()  # Add an empty line between collections



# Run the Flask application
if __name__ == '__main__':

    app.run(debug=True)
