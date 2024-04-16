from pymongo import MongoClient
from datetime import datetime
from classes import Flight

# MongoDB connection URI
uri = "mongodb://localhost:27017/"

# Connect to MongoDB server
client = MongoClient(uri)

# Access the 'Air_line_management' database
db = client['Air_line_management']

# Access the 'flights' collection
flights_collection = db['Flight']

# Function to calculate duration between two datetime objects
def calculate_duration(departure_time, arrival_time):
    duration = arrival_time - departure_time
    return duration.total_seconds() // 60  # Convert to minutes

# Function to add a flight to the database
# Function to add a flight to the database
def add_flight():
    flight_id = input("Enter flight ID: ")
    airline = input("Enter airline: ")
    aircraft = input("Enter aircraft: ")
    departure_airport = input("Enter departure airport: ")
    departure_time_str = input("Enter departure time (YYYY-MM-DD HH:MM): ")
    departure_time = datetime.strptime(departure_time_str, "%Y-%m-%d %H:%M")
    arrival_airport = input("Enter arrival airport: ")
    arrival_time_str = input("Enter arrival time (YYYY-MM-DD HH:MM): ")
    arrival_time = datetime.strptime(arrival_time_str, "%Y-%m-%d %H:%M")
    
    # Calculate duration
    duration_minutes = calculate_duration(departure_time, arrival_time)
    
    if duration_minutes > 1080:
        print("Error: Duration exceeds 18 hours (1080 minutes). Please enter a valid duration.")
        return

    passenger_capacity = int(input("Enter passenger capacity: "))
    ticket_price = float(input("Enter ticket price: "))
    available_seats = int(input("Enter available seats: "))
    status = input("Enter status: ")

    # Display flight details for confirmation
    print("\nFlight Details:")
    print("Flight ID:", flight_id)
    print("Airline:", airline)
    print("Aircraft:", aircraft)
    print("Departure Airport:", departure_airport)
    print("Departure Time:", departure_time)
    print("Arrival Airport:", arrival_airport)
    print("Arrival Time:", arrival_time)
    print("Duration:", duration_minutes, "minutes")
    print("Passenger Capacity:", passenger_capacity)
    print("Ticket Price:", ticket_price)
    print("Available Seats:", available_seats)
    print("Status:", status)

    # Ask for confirmation
    confirm = input("\nConfirm adding this flight to the database? (yes/no): ")
    if confirm.lower() != "yes":
        print("Flight addition cancelled.")
        return

    # Create a Flight object
    flight = Flight(flight_id, airline, aircraft, departure_airport, departure_time,
                    arrival_airport, arrival_time, duration_minutes, passenger_capacity,
                    ticket_price, available_seats, status)

    # Insert the flight document into the collection
    flights_collection.insert_one(flight.__dict__)
    print("Flight added successfully!")


# Call the add_flight function to add a flight
add_flight()

# Close the MongoDB connection
client.close()

