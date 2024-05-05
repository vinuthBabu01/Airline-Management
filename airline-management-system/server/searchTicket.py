from flask import Blueprint, jsonify,request
from bookticket import Ticket

# Create a Blueprint object named 'search_ticket_blueprint' with the URL prefix '/tickets'
search_ticket_blueprint = Blueprint('search_ticket', __name__, url_prefix='/tickets')


class SearchTicket(Ticket):
    def __init__(self,ticket_id, passenger_name, flight_number, departure_date,gender,email,phoneNo,requiredSeats,origin,price,durationInMinutes,destination, status='Active'):
        super().__init__(ticket_id, passenger_name, flight_number, departure_date,gender,email,phoneNo,requiredSeats,origin,price,durationInMinutes,destination, status='Active')

    def get_ticket_details(self, ticket_id):
        # Assuming tickets_collection is defined in the Ticket class
        ticket = self.tickets_collection.find_one({'ticket_id': ticket_id})
        
        if ticket:
            # Remove the MongoDB _id field from the response
            ticket.pop('_id', None)
            response = jsonify(message='Ticket fetched successfully', ticket_info=ticket)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
        else:
            error = jsonify(message=f"Ticket with ID {ticket_id} not found")
            error.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
            error.headers.add('Access-Control-Allow-Credentials', 'true')
            return error, 400

# Define the route for fetching ticket details based on ticket ID
@search_ticket_blueprint.route('/ticketId', methods=['POST'])
def search_ticket():
    data = request.get_json()
    ticket_id = data.get('ticket_id')
    search_ticket_instance = SearchTicket(ticket_id, passenger_name= '', flight_number= '', departure_date= '',gender= '',email= '',phoneNo= '',requiredSeats='',origin='',price='',durationInMinutes='',destination='', status='Active')
    return search_ticket_instance.get_ticket_details(ticket_id)

