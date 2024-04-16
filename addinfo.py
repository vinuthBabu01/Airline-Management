from pymongo import MongoClient

from classes import Airline, Airport

'''
def add_airport_to_db(airport):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Air_line_management"]
    airports_collection = db["airports"]
    airports_collection.insert_one(airport.to_dict())
    client.close()

# Add Airport
airport_code = input("Enter Airport Code: ")
airport_name = input("Enter Airport Name: ")
location_city = input("Enter Airport City: ")
location_country = input("Enter Airport Country: ")
timezone = input("Enter Airport Timezone: ")
capacity = int(input("Enter Airport Capacity: "))

airport = Airport(
    airport_code=airport_code,
    name=airport_name,
    location={"city": location_city, "country": location_country},
    timezone=timezone,
    capacity=capacity
)
add_airport_to_db(airport)
print("Airport added to the database.")'''

def list_all_airlines():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Air_line_management"]
    airlines_collection = db["airlines"]
    airlines = airlines_collection.find({})
    for airline in airlines:
        print(airline)
    client.close()
    
print("All Airlines:")
list_all_airlines()
'''
def check_airline_in_db(airline_name):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Air_line_management"]
    airlines_collection = db["airlines"]
    airline = airlines_collection.find_one({"name": airline_name})
    client.close()
    return airline is not None

# Example usage
airline_name = input("Enter the airline name to check: ")
if check_airline_in_db(airline_name):
    print(f"The airline '{airline_name}' exists in the database.")
else:
    print(f"The airline '{airline_name}' does not exist in the database.")'''
    


# Import MongoClient and DocumentTooLarge
from pymongo import MongoClient
from pymongo.errors import DocumentTooLarge
from datetime import datetime

# MongoDB connection URI
uri = "mongodb://localhost:27017/"

# Connect to MongoDB server
client = MongoClient(uri)

# Access or create the database named 'Air_line_management'
db = client['Air_line_management']

# Access the 'airlines' collection
airlines_collection = db['airlines']

# Define a function to insert an airline document into the collection
def insert_airline(airline):
    try:
        airlines_collection.insert_one(airline)
        print("Airline document inserted successfully")
    except DocumentTooLarge:
        print("Airline document is too large")

# Define airline documents
airlines = [
    {
        "name": "Air India",
        "location": {
            "city": "Mumbai",
            "country": "India"
        },
        "flights": []
    },
    {
        "name": "Emirates",
        "location": {
            "city": "Dubai",
            "country": "United Arab Emirates"
        },
        "flights": []
    },
    {
        "name": "Delta",
        "location": {
            "city": "Atlanta",
            "country": "United States"
        },
        "flights": []
    }
]

# Insert airline documents into the collection
for airline in airlines:
    insert_airline(airline)

# Close the MongoDB connection
client.close()



