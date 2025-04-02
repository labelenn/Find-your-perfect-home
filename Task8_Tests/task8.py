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
    """
    # TODO: Copy and paste your code from task 6
    raise NotImplementedError


def find_matching_properties(props: List[Property], house_importance: dict) -> List[Property]:
    """
    THis method recevied a list of all properties and a dictionary that
    contains the house importance criteria from a user's request
    and returns a list of Property objects that match the user's request
    """
    # TODO: Copy and paste your code from task 6
    raise NotImplementedError


def create_response_dict(scored_properties: dict) -> dict:
    """
    This method takes in a dictionary that has the property objects
    and their star scores and creates a dictionary in JSON format
    that can be written into a file
    """
    # TODO: Copy and paste your code from task 6
    raise NotImplementedError


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
    """
    # TODO: Copy and paste your code from task 6
    # and create a JSON file
    raise NotImplementedError


if __name__ == '__main__':
    response_dict, matched_props = produce_star_scores('request.json', 'melbourne_properties.csv',
                                                       ['melbourne_medical.csv', 'melbourne_schools.csv',
                                                        'train_stations.csv', 'sport_facilities.csv'])
    print(f"{len(matched_props)} properties matched with the user's request")
    respond(response_dict)
    # Check if response.json exists in the current directory
    if os.path.exists("/home/response.json"):
        print("File created successfully")
    else:
        print("File not created. Some Error occurred")
