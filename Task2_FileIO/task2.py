# DO NOT DELETE THIS LINE
from haversine import haversine_distance

def extract_property_information(property_string: str) -> dict:
    """
    Extracts the property"s information from the given string.

    Arguments:
        property_string (str): a string containing the property"s information in the following format:
        "<prop_id>,<full_address>,<bedrooms>,<bathrooms>,<parking_spaces>,<latitude>,<longitude>,<floor_number>,<land_area>,<floor_area>,<price>,<property_features>"

    Returns:
        dict: a dictionary containing the property's information. The keys are the name of the property's attributes and the values are the corresponding values.
    """
    info = property_string.split(",")

    property_info =  {}
    property_info["prop_id"] = info[0]

    # We can split the address with space as the delimiter, and check if the first element contains a "/".
    # This will help us determine if it"s an apartment or a house, taking into account that a "/" can appear else where in the address.
    property_info["prop_type"] = "apartment" if "/" in info[1].split(" ")[0] else "house"

    property_info["full_address"] = info[1]
    property_info["suburb"] = info[1].split(" ")[-3]
    property_info["bedrooms"] = int(info[2])
    property_info["bathrooms"] = int(info[3])
    property_info["parking_spaces"] = int(info[4])
    property_info["latitude"] = float(info[5])
    property_info["longitude"] = float(info[6])

    if property_info["prop_type"] == "apartment":
        property_info["floor_number"] = int(info[7])
    else:
        property_info["land_area"] = int(info[8])

    property_info["floor_area"] = int(info[9])
    property_info["price"] = int(info[10])
    property_info["property_features"] = info[11].split(";") if info[10] != "" else []

    return property_info

def extract_station_information(station_string: str) -> dict:
    """
    Extracts the train station's information from the given string.

    Arguments:
        station_string (str): a string containing the train station's information in the following format:
        "<stop_id>,<stop_name>,<stop_lat>,<stop_lon>"

    Returns:
        dict: a dictionary containing the station's information. The keys are the name of the station's attributes and the values are the corresponding values.
    """
    info = station_string.split(",")
    station_info = {}
    station_info["stop_id"] = info[0]
    station_info["stop_name"] = info[1]
    station_info["stop_lat"] = float(info[2])
    station_info["stop_lon"] = float(info[3])
    return station_info

def process_properties(file_name: str) -> dict:
    """
    Reads the properties" information from the given file name.

    Arguments:
        file_name (str): the name of the file containing the properties information.

    Returns:
        dict: a dictionary containing dictionary(s) of property(s). The keys are the property IDs and the values are the corresponding dictionary containing the property information.
    """

    file_handle = open(file_name, "r")
    file_handle.readline() # Skip the header
    properties = {}

    # Iterate through each line in the file and extract the property information.
    # Add the property information to the properties dictionary.
    for line in file_handle:
        prop_info = extract_property_information(line)
        properties[prop_info["prop_id"]] = prop_info

    return properties
        
def process_stations(file_name: str) -> dict:
    """
    Reads the train stations" information from the given file name.

    Arguments:
        file_name (str): the name of the file containing the train stations information.

    Returns:
        dict: a dictionary containing the train stations' information. The keys are the station IDs and the values are the corresponding dictionary containing the station information.
    """
    file_handle = open(file_name, "r")
    dict_keys = file_handle.readline().strip().split(",")
    stations = {}
    for line in file_handle:
        station_info = extract_station_information(line)
        stations[station_info["stop_id"]] = station_info

    return stations

def nearest_station(properties: dict, stations: dict, prop_id: str) -> str:
    """
    Finds the nearest train station to the given property ID.

    Arguments:
        properties (dict): a dictionary containing dictionary(s) of property(s). The keys are the property IDs and the values are the corresponding dictionary containing the property information.
        stations (dict): a dictionary containing the train stations' information. The keys are the station IDs and the values are the corresponding dictionary containing the station information.
        prop_id (str): the property ID to find the nearest station for.

    Returns:
        str: the name of the nearest station to the property
    """
    prop = properties[prop_id]
    prop_lat = prop["latitude"]
    prop_lon = prop["longitude"]
    min_distance = float("inf")
    nearest_station = ""

    # Iterate through all the stations and calculate the distance between the property and the station.
    # If the distance is less than the minimum distance, update the minimum distance and the nearest station.
    for key in stations:
        station_lat = stations[key]["stop_lat"]
        station_lon = stations[key]["stop_lon"]
        distance = haversine_distance(prop_lat, prop_lon, station_lat, station_lon)
        if distance < min_distance:
            min_distance = distance
            nearest_station = stations[key]["stop_name"]

    return nearest_station

def main():
    """
    You need not touch this function, if your 
    code is correct, this function will work as intended 
    """
    # Process the properties
    properties_file = "sample_properties.csv"
    properties = process_properties(properties_file)

    # Process the train stations
    stations_file = "train_stations.csv"
    stations = process_stations(stations_file)

    # Check the validity of stations
    sample_prop = "P10001"
    print(f"The nearest station for property {sample_prop} is {nearest_station(properties, stations, sample_prop)}")
    


if __name__ == "__main__":
    main()