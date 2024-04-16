from pymongo import MongoClient

# Function to check data in the Airline collection
def check_airline_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Air_line_management"]
    airlines_collection = db["airlines"]
    airlines = airlines_collection.find()

    print("Airline Collection Data:")
    for airline in airlines:
        print(airline)
    
    client.close()

# Function to add an airline to the Airline collection
def add_airline(airline_data):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Air_line_management"]
    airlines_collection = db["airlines"]
    
    # Insert the airline data
    result = airlines_collection.insert_one(airline_data)
    print("Airline added successfully with ObjectID:", result.inserted_id)

    client.close()

# Example usage to check airline data
check_airline_data()

# Example usage to add an airline
new_airline_data = {
    "name": "Example Airways",
    "code": "EXA",
    "country": "United States"
}
add_airline(new_airline_data)
