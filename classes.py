# classes.py

class Account:
    def __init__(self, username, password, user_role):
        self.username = username
        self.password = password
        self.user_role = user_role

    def authenticate(self, entered_username, entered_password):
        return self.username == entered_username and self.password == entered_password

    def get_user_role(self):
        return self.user_role


class Flight:
    def __init__(self, flight_id, airline, aircraft, departure_airport, departure_time, arrival_airport,
                 arrival_time, duration_minutes, passenger_capacity, ticket_price, available_seats, status):
        self._flight_id = flight_id
        self._airline = airline
        self._aircraft = aircraft
        self._departure_airport = departure_airport
        self._departure_time = departure_time
        self._arrival_airport = arrival_airport
        self._arrival_time = arrival_time
        self._duration_minutes = duration_minutes
        self._passenger_capacity = passenger_capacity
        self._ticket_price = ticket_price
        self._available_seats = available_seats
        self._status = status

    def update_status(self, new_status):
        self._status = new_status

    # Other methods for managing flight details...


class FlightInstance(Flight):
    def __init__(self, departure_time, gate, status):
        # Calling superclass (Flight) constructor to initialize common attributes
        super().__init__(departure_time=departure_time, status=status)
        self._gate = gate

    def update_gate(self, new_gate):
        self._gate = new_gate

    # Additional methods specific to FlightInstance...



class Airport:
    def __init__(self, airport_code, name, location, timezone, capacity):
        self.airport_code = airport_code
        self.name = name
        self.location = location
        self.timezone = timezone
        self.capacity = capacity

    def to_dict(self):
        return {
            "airport_code": self.airport_code,
            "name": self.name,
            "location": self.location,
            "timezone": self.timezone,
            "capacity": self.capacity
        }

       

class Airline:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.flights = []  # Empty list to store flights allocated to this airline later
