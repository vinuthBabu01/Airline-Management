from flask import Flask, Blueprint,request, jsonify
from flask_cors import CORS
from datetime import datetime
import pymongo
import requests
import json

from dbconnection import get_mongo_collections


# Create a Flask app instance
app = Flask(__name__)
# Enable CORS for all origins on all routes
CORS(app, supports_credentials=True)

# MongoDB  details
collections = get_mongo_collections()

collection = collections['airports']

# Create a Blueprint object named 'login_blueprint' with the URL prefix '/auth'
search_blueprint = Blueprint('search', __name__, url_prefix='/search')

# Define route for airport search
@search_blueprint.route('/searchflight', methods=['POST'])
def searchflight():
    
    data = request.get_json()

    entity = getEntityData(data)

    to_entity_id = entity.get('destinationId')

    from_entity_id = entity.get('originId')
    depart_date = data.get('depart_date')
 
    response= fetch_flight_data(from_entity_id, to_entity_id,depart_date)
    if response.status_code == 200:
        flight_data = parse_flight_data(response.text)
        response = jsonify(message='data fetched successfully', flight_data=flight_data)
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 200
    else:
        response = jsonify(message=response.text)
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response, 401

def parse_flight_data(response):
    parsed_data = json.loads(response)
    itineraries = parsed_data.get("data", {}).get("itineraries", [])
    
    flights_info = []
    for itinerary in itineraries:
        legs = itinerary.get("legs", [])
        for leg in legs:
            duration_in_minutes = leg.get("durationInMinutes", "")
            logo_url = leg.get("carriers", {}).get("marketing", [{}])[0].get("logoUrl", "")
            carrier_name = leg.get("carriers", {}).get("marketing", [{}])[0].get("name", "")
            formatted_price = itinerary.get("price", {}).get("formatted", "")
            departure_time = leg.get("departure", "")
            arrival_time = leg.get("arrival", "")
            flight_number = leg.get("segments", [{}])[0].get("flightNumber", "")
            flights_info.append({
                "durationInMinutes": duration_in_minutes,
                "logoUrl": logo_url,
                "carrierName": carrier_name,
                "formattedPrice": formatted_price,
                "departureTime": departure_time,
                "arrivalTime": arrival_time,
                "flightNumber":flight_number
            })
    
    return flights_info

def getEntityData(data):
    origin_code = data.get("origin")
    destination_code = data.get("destination")
    
    # Search for origin airport
    origin_airport = collection.find_one({"iata": origin_code})
    if origin_airport:
        origin_id = origin_airport.get("id")
    else:
        print(f"No record found for origin airport with IATA code '{origin_code}'")
        return (f"No record found for origin airport with IATA code '{origin_code}'")
    
    # Search for destination airport
    destination_airport = collection.find_one({"iata": destination_code})
    if destination_airport:
        destination_id = destination_airport.get("id")
    else:
        print(f"No record found for destination airport with IATA code '{destination_code}'")
        return (f"No record found for destination airport with IATA code '{destination_code}'")
    
    return {"originId": origin_id, "destinationId": destination_id}


def fetch_flight_data(from_entity_id, to_entity_id, depart_date):
    url = f"https://sky-scanner3.p.rapidapi.com/flights/search-one-way?fromEntityId={from_entity_id}&toEntityId={to_entity_id}&departDate={depart_date}&market=US&locale=en-US&currency=USD&adults=1&cabinClass=economy"
    headers = {
        'X-RapidAPI-Key': "145ff162f4msh8d7cb62ee6e7271p1a67d2jsnd92573132ffe",
        'X-RapidAPI-Host': "sky-scanner3.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    return response

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

