def extract_information(property_string: str) -> dict:
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
    - property_features <list of strings>: a semi-color separated list of the features of the property. Could include solar, air conditioning, dishwasher, floorboards, central heating, etc.
      -- this can have 0 items, and if it does, make an empty list
    '''
    raise NotImplementedError

def add_feature(property_dict: dict, feature: str) -> None:
    raise NotImplementedError

def remove_feature(property_dict: dict, feature: str) -> None:
    raise NotImplementedError

def main():
    sample_string = "P10001,3 Antrim Place Langwarrin VIC 3910,4,2,2,-38.16655678,145.1838435,,608,257,870000,dishwasher;central heating"
    property_dict = extract_information(sample_string)
    print(f"The first property is at {property_dict['full_address']} and is valued at ${property_dict['price']}")

    sample_string_2 = "P10002,G01/7 Rugby Road Hughesdale VIC 3166,2,1,1,-37.89342337,145.0862616,1,,125,645000,dishwasher;air conditioning;balcony"
    property_dict_2 = extract_information(sample_string_2)

    print(f"The second property is in {property_dict_2['suburb']} and is located on floor {property_dict_2['floor_number']}")

    add_feature(property_dict, 'electric hot water')
    print(f"Property {property_dict['prop_id']} has the following features: {property_dict['property_features']}")

if __name__ == '__main__':
    main()