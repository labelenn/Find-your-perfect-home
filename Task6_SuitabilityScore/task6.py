import os
import json
from typing import List, Tuple, Dict
from parent_property import Property
from child_properties import House, Apartment
from amenity import Amenity
from ingestion import ingest_files
from score import *

def read_request(request_filename: str) -> Tuple[dict, dict]:
    """
    This method reads a request file in json format
    and returns two dictionaries; one containing the
    house_importance features and one containing the 
    amenity_importance features.

    Arguments:
        request_filename (str): the name of the request file

    Returns:
        Tuple[dict, dict]: a tuple containing the house_importance
        and amenities_accessibility dictionaries
    """
    with open(request_filename, 'r') as file:
        request = json.load(file)['request']
        return request['house_importance'], request['amenities_accessibility']

def find_matching_properties(props: List[Property], house_importance: dict) -> List[Property]:
    """
    THis method recevied a list of all properties and a dictionary that
    contains the house importance criteria from a user's request 
    and returns a list of Property objects that match the user's request

    Arguments:
        props (List[Property]): a list of all properties
        house_importance (dict): a dictionary containing the house importance criteria

    Returns:
        List[Property]: a list of properties that match the user
    """
    matching_properties = props

    # Full match
    suburb = house_importance['suburb'] if 'suburb' in house_importance.keys() else None
    property_type = house_importance['property_type'] if 'property_type' in house_importance.keys() else None
    property_features = house_importance['property_features'] if 'property_features' in house_importance.keys() else None

    # Treat these as ceiling values. Properties that have these values or less than these values will be considered
    price = house_importance['price'] if 'price' in house_importance.keys() else None
    floor_number = house_importance['floor_number'] if 'floor_number' in house_importance.keys() else None

    # Treat these as baseline values. Properties that have these values or greater will be considered
    floor_area = house_importance['floor_area'] if 'floor_area' in house_importance.keys() else None
    land_area = house_importance['land_area'] if 'land_area' in house_importance.keys() else None
    bedrooms = house_importance['bedrooms'] if 'bedrooms' in house_importance.keys() else None
    bathrooms = house_importance['bathrooms'] if 'bathrooms' in house_importance.keys() else None
    parking_spaces = house_importance['parking_spaces'] if 'parking_spaces' in house_importance.keys() else None

    # Filter out properties per information provided
    if property_type is not None:
        matching_properties = [x for x in props if x.get_prop_type() == property_type]
    if suburb is not None:
        matching_properties = [x for x in matching_properties if x.get_suburb() == suburb]
    if property_features is not None:
        for prop in matching_properties:
            if property_features not in prop.get_property_features():
                matching_properties.remove(prop)

    if floor_area is not None:
        matching_properties = [x for x in matching_properties if x.get_floor_area() >= floor_area]
    if land_area is not None:
        matching_properties = [x for x in matching_properties if x.get_land_area() >= land_area]
    if bedrooms is not None:
        matching_properties = [x for x in matching_properties if x.get_bedrooms() >= bedrooms]
    if bathrooms is not None:
        matching_properties = [x for x in matching_properties if x.get_bathrooms() >= bathrooms]
    if parking_spaces is not None:
        matching_properties = [x for x in matching_properties if x.get_parking_spaces() >= parking_spaces]

    if price is not None:
        matching_properties = [x for x in matching_properties if x.get_price() <= price]
    if floor_number is not None:
        matching_properties = [x for x in matching_properties if x.get_floor_number() <= floor_number]

    return matching_properties

def create_response_dict(scored_properties: dict) -> dict:
    """
    This method takes in a dictionary that has the property objects 
    and their star scores and creates a dictionary in JSON format 
    that can be written into a file

    Arguments:
        scored_properties (dict): a dictionary containing the property objects and their star scores

    Returns:
        dict: a dictionary that can be written into a file
    """
    response_dict = { "properties": []}
    for key in scored_properties.keys():
        response_dict['properties'].append({"property_id": scored_properties[key].get_prop_id(), "star_score": key})

    return response_dict

def produce_star_scores(request_filename: str, properties_file: str, amenities_files: List[str]) -> dict:
    # Read the properties and amenities
    medical_file, schools_file, train_stations, sport_facilities = amenities_files
    props, amenities = ingest_files(properties_file, medical_file, schools_file, train_stations, sport_facilities)

    # Read the request and get the dictionaries of house_importance and amenity_accessibility
    house_importance, amenity_accessibility = read_request(request_filename)

    # Collect properties that match the property criteria
    matched_props = find_matching_properties(props, house_importance)

    # Score properties using the amenity amenity_accessibility dictionary
    prop_scores = [score_property(x, amenities, amenity_accessibility) for x in matched_props]

    # Now, we can normalise the scores that we just got
    norm_scores = normalise_scores(prop_scores)

    # Create a collection matching property object to Score
    prop_scored = dict(zip(norm_scores, matched_props))

    # Create a response dictionary
    response_dict = create_response_dict(prop_scored)
    
    # Return the response dictionary from step 3 and the list of matching property family objects
    return response_dict, matched_props

def respond(response_dict: dict) -> None:
    """
    This function reads a response dictionary and creates a JSON 
    file based on the content of the response dictionary

    Arguments:
        response_dict (dict): a dictionary that contains the response
    """
    response_dict['properties'] = sorted(response_dict['properties'], key=lambda x: x['star_score'], reverse=True)

    with open('response.json', 'w') as file:
        json.dump(response_dict, file)

if __name__ == '__main__':
    response_dict, matched_props = produce_star_scores('request.json', 'melbourne_properties.csv', ['melbourne_medical.csv', 'melbourne_schools.csv', 'train_stations.csv', 'sport_facilities.csv'])
    print(f"{len(matched_props)} properties matched with the user's request")
    respond(response_dict)
    # Check if response.json exists in the current directory
    if os.path.exists("/home/response.json"):
        print("File created successfully")
    else:
        print("File not created. Some Error occurred")
