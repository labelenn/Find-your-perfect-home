# DO NOT DELETE THIS LINE
from haversine import haversine_distance

def extract_property_information(property_string: str) -> dict:
    '''
    Extracts the property's information from the given string, and returns a dictionary containing the information.
    The dictionary will contain the following:
    - prop_id <str>: the property's ID
    - prop_type <str>: the type of the property (either 'house' or 'apartment')
    - full_address <str>: this is the address of the property
    -- if it's a house, it will be in the format of "<street number> <street name> <street type> <suburb> <state code> <postcode>"
    -- if it's an apartment, it will be in the format of "<apartment number>/<street number> <street name> <street type> <suburb> <state code> <postcode>"
    - suburb <str>: the suburb of the property
    - bedrooms <int>: the number of bedrooms in the property
    - bathrooms <int>: the number of bathrooms in the property
    - parking_spaces <int>: the number of car spaces in the property
    - latitude <float>: the latitude of the property
    - longitude <float>: the longitude of the property
    - floor_number <int>: the floor number of the property (ONLY if it's an apartment. This will be excluded if it's a house)
    - land_area <int>: land area in m^2 (ONLY if it's a house. This will be excluded if it's an apartment)
    - floor_area <int>: floor area in m^2 of the property
    - price <int>: the predicted price of the property
    - property_features <list of strings>: a semi-colon separated list of the features of the property. Could include solar, air conditioning, dishwasher, floorboards, central heating, etc.
    -- this can have 0 items, and if it does, make an empty list
    '''
    info = property_string.split(',')

    property_info =  {}
    property_info['prop_id'] = info[0]

    # We can split the address with space as the delimiter, and check if the first element contains a '/'.
    # This will help us determine if it's an apartment or a house, taking into account that a '/' can appear else where in the address.
    property_info['prop_type'] = 'apartment' if '/' in info[1].split(' ')[0] else 'house'

    property_info['full_address'] = info[1]
    property_info['suburb'] = info[1].split(' ')[-3]
    property_info['bedrooms'] = int(info[2])
    property_info['bathrooms'] = int(info[3])
    property_info['parking_spaces'] = int(info[4])
    property_info['latitude'] = float(info[5])
    property_info['longitude'] = float(info[6])

    if property_info['prop_type'] == 'apartment':
        property_info['floor_number'] = int(info[7])
    else:
        property_info['land_area'] = int(info[8])

    property_info['floor_area'] = int(info[9])
    property_info['price'] = int(info[10])
    property_info['property_features'] = info[11].split(';') if info[10] != '' else []

    return property_info

def extract_station_information(station_string: str) -> dict:
    '''
    Extracts the train station's information from the given string, and returns a dictionary containing the information.
    The dictionary will contain the following:
    - stop_id <str>: the station's stop ID
    - stop_name <str>: the name of the station
    - stop_lat <float>: the latitude of the station
    - stop_lon <float>: the longitude of the station
    '''
    info = station_string.split(',')
    station_info = {}
    station_info['stop_id'] = info[0]
    station_info['stop_name'] = info[1]
    station_info['stop_lat'] = float(info[2])
    station_info['stop_lon'] = float(info[3])
    return station_info

def process_properties(file_name: str) -> dict:
    '''
    Reads the properties' information from the given file and returns a dictionary.
    The diction will have the property's ID as the key, and the value will be another dictionary for the property's information (same structure as Task 1).
    '''

    file_handle = open(file_name, 'r')
    file_handle.readline() # Skip the header
    properties = {}

    for line in file_handle:
        prop_info = extract_property_information(line)
        properties[prop_info['prop_id']] = prop_info

    return properties
        
def process_stations(file_name: str) -> dict:
    '''
    Reads the train stations' information from the given file and returns a dictionary.
    The diction will have the station's stop ID as the key, and the value will be another dictionary for the station's information.
    '''
    file_handle = open(file_name, 'r')
    dict_keys = file_handle.readline().strip().split(',')
    stations = {}
    for line in file_handle:
        station_info = extract_station_information(line)
        stations[station_info['stop_id']] = station_info

    return stations

def nearest_station(properties: dict, stations: dict, prop_id: str) -> str:
    '''
    Finds the nearest train station to the given property ID.
    It returns the name of the nearest station.
    '''
    prop = properties[prop_id]
    prop_lat = prop['latitude']
    prop_lon = prop['longitude']
    min_distance = float('inf')
    nearest_station = ''

    for key in stations:
        station_lat = stations[key]['stop_lat']
        station_lon = stations[key]['stop_lon']
        distance = haversine_distance(prop_lat, prop_lon, station_lat, station_lon)
        if distance < min_distance:
            min_distance = distance
            nearest_station = stations[key]['stop_name']

    return nearest_station

def main():
    """
    You need not touch this function, if your 
    code is correct, this function will work as intended 
    """
    # Process the properties
    properties_file = 'sample_properties.csv'
    properties = process_properties(properties_file)

    # Process the train stations
    stations_file = 'train_stations.csv'
    stations = process_stations(stations_file)

    # Check the validity of stations
    sample_prop = 'P10001'
    print(f"The nearest station for property {sample_prop} is {nearest_station(properties, stations, sample_prop)}")
    


if __name__ == '__main__':
    main()