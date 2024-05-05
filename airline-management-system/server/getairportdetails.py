import requests
import pymongo

# MongoDB connection details
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
DATABASE_NAME = "Air_line_management"
COLLECTION_NAME = "airports"

# API details
URL = "https://sky-scanner3.p.rapidapi.com/flights/airports"
HEADERS = {
    "X-RapidAPI-Key": "145ff162f4msh8d7cb62ee6e7271p1a67d2jsnd92573132ffe",
    "X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
}

# Fetch data from the API
response = requests.get(URL, headers=HEADERS)
data = response.json()

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Insert data into MongoDB collection
if data.get("status") == True:
    airports = data.get("data", [])
    for airport in airports:
        collection.insert_one(airport)
    print("Data inserted successfully into MongoDB collection 'airports'")
else:
    print("API request failed:", data.get("message"))
