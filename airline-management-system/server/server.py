from flask import Flask, request, jsonify
from flask_cors import CORS
from login import Users, login_blueprint  # Import the Users class and login_blueprint from login.py
from searchairports import search_blueprint
from bookticket import ticket_blueprint
from searchTicket import search_ticket_blueprint
from dbconnection import get_mongo_collections

# Create a Flask app instance
app = Flask(__name__)
# Enable CORS for all origins on all routes
CORS(app, supports_credentials=True)

# Initialize Users service
users_service = Users()  # Assuming 'Users' is a valid class representing a service

# Define route within the login blueprint
@login_blueprint.route('/auth', methods=['POST'])
@search_blueprint.route('/search',methods=['POST'])
@ticket_blueprint.route('/ticket',methods=['POST'])
@search_ticket_blueprint.route('/tickets',methods=['POST'])
def handle_auth_request():
    data = request.get_json()
    action = data.get('action')

    response = users_service.handle_request(data)
    return response

# Register the login blueprint with the Flask app
app.register_blueprint(login_blueprint, url_prefix='/auth')
app.register_blueprint(search_blueprint, url_prefix='/search')
app.register_blueprint(ticket_blueprint, url_prefix='/ticket')
app.register_blueprint(search_ticket_blueprint, url_prefix='/tickets')


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

