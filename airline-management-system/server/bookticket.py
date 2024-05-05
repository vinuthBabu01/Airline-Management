from flask import Flask, Blueprint, jsonify, request
from dbconnection import get_mongo_collections
import random

# Create a Blueprint object named 'ticket_blueprint' with the URL prefix '/ticket'
ticket_blueprint = Blueprint('ticket', __name__, url_prefix='/ticket')

collections = get_mongo_collections()

class Ticket:
    tickets_collection = collections['tickets']
    def __init__(self, ticket_id, passenger_name, flight_number, departure_date,gender,email,phoneNo,requiredSeats,origin,price,durationInMinutes,destination, status='Active'):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.flight_number = flight_number
        self.departure_date = departure_date
        self.status = status
        self.gender=gender
        self.email=email
        self.phoneNo=phoneNo
        self.requiredSeats=requiredSeats
        self.origin=origin
        self.price=price
        self.durationInMinutes=durationInMinutes
        self.destination=destination
        pass


    def generate_ticket(self):
        raise NotImplementedError("Subclasses must implement generate_ticket method")


class BookTicket(Ticket):
    def __init__(self, ticket_id, passenger_name, flight_number, departure_date,gender,email,phoneNo,requiredSeats,origin,price,durationInMinutes,destination):
        super().__init__(ticket_id, passenger_name, flight_number, departure_date,gender,email,phoneNo,requiredSeats,origin,price,durationInMinutes,destination)

    def generate_ticket(self):
        return f"Ticket ID: {self.ticket_id}, Passenger: {self.passenger_name}, Flight Number: {self.flight_number}, Departure Date: {self.departure_date}"


class CancelTicket(Ticket):
    def __init__(self, ticket_id, passenger_name, cancellation_reason):
        super().__init__(ticket_id, passenger_name)
        self.cancellation_reason = cancellation_reason

    def generate_ticket(self):
        return f"Ticket ID: {self.ticket_id}, Passenger: {self.passenger_name}, Cancellation Reason: {self.cancellation_reason}"

def generate_ticket_id():
    prefix = "TA-"
    random_number = ''.join(random.choices('0123456789', k=10))
    ticket_id = prefix + random_number
    return ticket_id

# Define the route for booking a ticket within the ticket blueprint
@ticket_blueprint.route('/book', methods=['POST'])
def book_ticket():
    data = request.get_json()
    ticket_id = generate_ticket_id(),
    firstName = data.get('firstName'),
    lastName = data.get('lastName'),
    gender=data.get('gender'),
    email=data.get('email'),
    phoneNo=data.get('phoneNo'),
    requiredSeats=data.get('requiredSeats'),
    origin=data.get('origin'),
    destination=data.get('destination'),
    price=data.get('price'),
    durationInMinutes=data.get('durationInMinutes'),
    flight_number = data.get('flightId'),
    departure_date = data.get('depart_date')
    
    passenger_name = firstName + lastName
    book_ticket = BookTicket(ticket_id, passenger_name, flight_number, departure_date,gender,email,phoneNo,requiredSeats,origin,price,durationInMinutes,destination)
    ticket_info = book_ticket.generate_ticket()
    
    # Store ticket data in MongoDB collection named 'tickets'
    collections['tickets'].insert_one({'ticket_id': ticket_id, 'passenger_name': passenger_name, 
                                       'flight_number': flight_number, 'departure_date': departure_date,
                                       'status': 'Active','passenger_name':passenger_name,'gender':gender,'email':email,'phoneNo':phoneNo,'requiredSeats':requiredSeats,'origin':origin,'price':price,"destination":destination,"durationInMinutes":durationInMinutes})
    
    response = jsonify(message='Ticket booked successfully', ticket_info=ticket_info, ticket_id=ticket_id)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response, 201

# Define the route for canceling a ticket within the ticket blueprint
@ticket_blueprint.route('/cancel', methods=['POST'])
def cancel_ticket():
    
    data = request.get_json()
    ticket_id = data.get('ticket_id')
    
    # Check if ticket exists
    ticket = collections['tickets'].find_one({'ticket_id': ticket_id, 'status':"Active"})
    print("ticket",ticket)
    if ticket:
        # Update ticket status to 'Cancelled'
        collections['tickets'].update_one({'ticket_id': ticket_id}, {'$set': {'status': 'Cancelled'}})
        response = jsonify(message='Ticket canceled successfully', ticket_info=f"Ticket ID: {ticket_id}, Status: Cancelled")
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 200
    else:
        error = jsonify(message=f"Ticket with ID {ticket_id} already Cancelled")
        error.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        error.headers.add('Access-Control-Allow-Credentials', 'true')
        return error, 400

# Export the blueprint for use in the Flask app

