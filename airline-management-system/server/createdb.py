#Install Mongodb before running the below query
#The below queries creates the database and the collections required
from pymongo import MongoClient
from pymongo.errors import DocumentTooLarge
from decimal import Decimal
from datetime import datetime

# MongoDB connection URI
uri = "mongodb://localhost:27017/"

# Connect to MongoDB server
client = MongoClient(uri)

# Access or create the database named 'Air_line_management'
db = client['Air_line_management']


tickets_collection = db['tickets']# Define the 'tickets' collection
users_collection = db['users']  # Define the 'users' collection
accounts_collection = db['accounts']  # Define the 'accounts' collection
flights_collection = db['flights']# Define the 'flights' collection
airports_collection = db['airports']# Define the 'airports' collection
crews_collection = db['crews']# Define the 'crews' collection

# Define a function to validate user documents
def validate_user(user):
    required_fields = ['email', 'first_name', 'last_name', 'phone_number', 'address', 'role', 'user_id']
    for field in required_fields:
        if field not in user:
            raise ValueError(f"User document is missing required field: {field}")
    if user['role'] not in ['admin', 'employee', 'customer']:
        raise ValueError("Invalid role value for user")

# Define a function to insert a user document into the collection
def insert_user(user):
    validate_user(user)
    user['created_at'] = datetime.now()  # Set 'created_at' timestamp
    user['updated_at'] = datetime.now()  # Set 'updated_at' timestamp
    try:
        users_collection.insert_one(user)
        print("User document inserted successfully")
    except DocumentTooLarge:
        print("User document is too large")


# Define a function to insert an account document into the collection
def insert_account(account):
    if 'username' not in account or 'password' not in account or 'user_id' not in account:
        raise ValueError("Account document is missing required fields (username, password, user_id)")
    try:
        accounts_collection.insert_one(account)
        print("Account document inserted successfully")
    except DocumentTooLarge:
        print("Account document is too large")

# Example user document
user_document = {
    'email': 'john.doe@example.com',
    'first_name': 'John',
    'last_name': 'Doe',
    'phone_number': '123-456-7890',
    'address': '123 Main St, Anytown',
    'role': 'customer',
    'user_id': 1  # User ID referencing the corresponding account
}

# Insert the example user document into the 'users' collection
insert_user(user_document)

# Example account document
account_document = {
    'username': 'john_doe',
    'password': 'password123',
    'user_id': 1  # User ID referencing the corresponding user
}

# Insert the example account document into the 'accounts' collection
insert_account(account_document)

# Define a function to validate ticket documents
def validate_ticket(ticket):
    required_fields = ['ticket_id', 'flight_id', 'user_id', 'passenger_name', 'passenger_email','passport_number','seat_class', 'status']
    for field in required_fields:
        if field not in ticket:
            raise ValueError(f"Ticket document is missing required field: {field}")
    if ticket['status'] not in ['booked', 'cancelled', 'completed']:
        raise ValueError("Invalid status value for ticket")

# Define a function to insert a ticket document into the collection
def insert_ticket(ticket):
    validate_ticket(ticket)
    # Convert Decimal to float for 'price' field
    ticket['price'] = float(ticket['price'])  # Convert Decimal to float
    try:
        tickets_collection.insert_one(ticket)
        print("Ticket document inserted successfully")
    except DocumentTooLarge:
        print("Ticket document is too large")

# Example ticket document
ticket_document = {
    'ticket_id': 1,
    'flight_id': 123,
    'user_id': 1,
    'passenger_name': 'John Doe',
    'passenger_email': 'john.doe@example.com',
    'seat_number': 'A1',
    'passport_number':'W8794SB1',
    'seat_class':'economy',
    'status': 'booked',
    'booking_date': '2024-04-10T12:00:00Z',
    'cancellation_date': None,
    'price': Decimal('250.00')  # Use Decimal class to represent price
}

# Insert the example ticket document into the collection
insert_ticket(ticket_document)


# Define a function to validate flight documents
def validate_flight(flight):
    required_fields = [
        'flight_id', 'airline', 'aircraft', 'departure_airport', 'departure_time',
        'arrival_airport', 'arrival_time', 'duration_minutes', 'passenger_capacity',
        'ticket_price', 'available_seats', 'status'
    ]
    for field in required_fields:
        if field not in flight:
            raise ValueError(f"Flight document is missing required field: {field}")
    if flight['status'] not in ['scheduled', 'boarding', 'delayed', 'departed', 'arrived', 'cancelled']:
        raise ValueError("Invalid status value for flight")

# Define a function to insert a flight document into the collection
def insert_flight(flight):
    validate_flight(flight)
    try:
        flights_collection.insert_one(flight)
        print("Flight document inserted successfully")
    except DocumentTooLarge:
        print("Flight document is too large")

# Example flight document
flight_document = {
    'flight_id': 'FL123',
    'airline': 'Example Airlines',
    'aircraft': 'Boeing 737',
    'departure_airport': 'JFK',
    'departure_time': datetime(2024, 4, 10, 12, 0),  # Example: April 10, 2024, 12:00 PM
    'arrival_airport': 'LAX',
    'arrival_time': datetime(2024, 4, 10, 15, 0),  # Example: April 10, 2024, 3:00 PM
    'duration_minutes': 180,
    'passenger_capacity': 200,
    'ticket_price': 250.00,
    'available_seats': 150,
    'status': 'scheduled'
}

# Insert the example flight document into the 'flights' collection
insert_flight(flight_document)

# Define a function to validate airport documents
def validate_airport(airport):
    required_fields = ['airport_code', 'name', 'location', 'timezone', 'capacity']
    for field in required_fields:
        if field not in airport:
            raise ValueError(f"Airport document is missing required field: {field}")
    if not isinstance(airport['location'], dict) or 'city' not in airport['location'] or 'country' not in airport['location']:
        raise ValueError("Invalid location format for airport")

# Define a function to insert an airport document into the collection
def insert_airport(airport):
    validate_airport(airport)
    try:
        airports_collection.insert_one(airport)
        print("Airport document inserted successfully")
    except DocumentTooLarge:
        print("Airport document is too large")

# Example airport document
airport_document = {
    'airport_code': 'JFK',
    'name': 'John F. Kennedy International Airport',
    'location': {
        'city': 'New York City',
        'country': 'United States'
    },
    'timezone': 'America/New_York',
    'capacity': 500  # Example: maximum number of airplanes it can operate in a day
}

# Insert the example airport document into the 'airports' collection
insert_airport(airport_document)

# Define a function to validate crew documents
def validate_crew(crew):
    required_fields = ['crew_id', 'crew_type', 'name', 'flights']
    for field in required_fields:
        if field not in crew:
            raise ValueError(f"Crew document is missing required field: {field}")
    if crew['crew_type'] not in ['pilot', 'co-pilot', 'flight_attendant', 'other']:
        raise ValueError("Invalid crew_type value for crew member")
    if not isinstance(crew['flights'], list) or not all(isinstance(flight, dict) and 'flight_number' in flight and 'role' in flight for flight in crew['flights']):
        raise ValueError("Invalid format for flights field in crew document")

# Define a function to insert a crew document into the collection
def insert_crew(crew):
    validate_crew(crew)
    try:
        crews_collection.insert_one(crew)
        print("Crew document inserted successfully")
    except DocumentTooLarge:
        print("Crew document is too large")

# Example crew document
crew_document = {
    'crew_id': 'C001',
    'crew_type': 'pilot',
    'name': 'John Smith',
    'flights': [
        {'flight_number': 'FL123', 'role': 'pilot'},
        {'flight_number': 'FL456', 'role': 'co-pilot'}
    ]
}

# Insert the example crew document into the 'crews' collection
insert_crew(crew_document)


# Close the MongoDB connection
client.close()
