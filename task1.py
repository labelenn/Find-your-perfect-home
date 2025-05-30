def extract_information(property_string: str) -> dict:
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
    

def add_feature(property_dict: dict, feature: str) -> None:
    """
    Adds a feature to the property_features key in the property dictionary.
    If the feature already exists, ignore the new value and don"t add anything.

    Arguments:
        property_dict (dict): a dictionary containing the property's information.
        feature (str): the feature to add to the property
    """
    if feature not in property_dict["property_features"]:
        property_dict["property_features"].append(feature)

def remove_feature(property_dict: dict, feature: str) -> None:
    """
    Removes a feature from the property_features key in the property dictionary.
    If the feature doesn"t exist, ignore the new value and don"t remove anything.

    Arguments:
        property_dict (dict): a dictionary containing the property's information.
        feature (str): the feature to remove from the property
    """
    if feature in property_dict["property_features"]:
        property_dict["property_features"].remove(feature)

def main():
    sample_string = "P10001,3 Antrim Place Langwarrin VIC 3910,4,2,2,-38.16655678,145.1838435,,608,257,870000,dishwasher;central heating"
    property_dict = extract_information(sample_string)
    print(f"The first property is at {property_dict["full_address"]} and is valued at ${property_dict["price"]}")

    sample_string_2 = "P10002,G01/7 Rugby Road Hughesdale VIC 3166,2,1,1,-37.89342337,145.0862616,1,,125,645000,dishwasher;air conditioning;balcony"
    property_dict_2 = extract_information(sample_string_2)

    print(f"The second property is in {property_dict_2["suburb"]} and is located on floor {property_dict_2["floor_number"]}")

    add_feature(property_dict, "electric hot water")
    print(f"Property {property_dict["prop_id"]} has the following features: {property_dict["property_features"]}")

if __name__ == "__main__":
    main()