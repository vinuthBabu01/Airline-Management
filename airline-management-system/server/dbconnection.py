import os
import pymongo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_mongo_collections():

    mongo_uri = os.getenv("MONGO_URI")
    db_name = os.getenv("DB_NAME")
    collection_names = os.getenv("COLLECTION_NAMES").split(",")
    # Connect to MongoDB server
    client = pymongo.MongoClient(mongo_uri)

    # Access the specific database
    db = client[db_name]

    # Initialize an empty dictionary to store collections
    collections = {}

    # Access each specified collection
    for collection_name in collection_names:
        collections[collection_name] = db[collection_name]

    return collections