from typing import Tuple, List, Union
from parent_property import Property

class House(Property):
    """
    House class that inherits from the Property class to represent a house object.

    Instance Variables:
        prop_id (str): the property's ID
        bedrooms (int): the number of bedrooms in the property
        bathrooms (int): the number of bathrooms in the property
        parking_spaces (int): the number of car spaces in the property
        full_address (str): the address of the property
        land_area (int): land area in m^2 of the property
        floor_area (int): floor area in m^2 of the property
        price (int): the predicted price of the property
        property_features (list of strings): a list of the features of the property. Could include solar, air conditioning, dishwasher, floorboards, central heating, etc.
        coordinates (tuple of floats): the latitude and longitude of the property
    """
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        land_area: int,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        """
        Initialises a house object.

        Arguments:
            prop_id (str): the property's ID
            bedrooms (int): the number of bedrooms in the property
            bathrooms (int): the number of bathrooms in the property
            parking_spaces (int): the number of car spaces in the property
            full_address (str): the address of the property
            land_area (int): land area in m^2 of the property
            floor_area (int): floor area in m^2 of the property
            price (int): the predicted price of the property
            property_features (list of strings): a list of the features of the property. Could include solar, air conditioning, dishwasher, floorboards, central heating, etc.
            coordinates (tuple of floats): the latitude and longitude of the property
        """
        self.prop_id = prop_id
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.parking_spaces = parking_spaces
        self.full_address = full_address
        self.land_area = land_area
        self.floor_area = floor_area
        self.price = price
        self.property_features = property_features
        self.coordinates = coordinates

    def get_land_area(self) -> int:
        """
        Returns:
            int: the land area of the property
        """
        return self.land_area
    
    def get_floor_number(self) -> None:
        """
        Returns:
            None: as a house does not have a floor number
        """
        return None

class Apartment(Property):
    """
    Apartment class that inherits from the Property class to represent an apartment object.

    Instance Variables:
        prop_id (str): the property's ID
        bedrooms (int): the number of bedrooms in the property
        bathrooms (int): the number of bathrooms in the property
        parking_spaces (int): the number of car spaces in the property
        full_address (str): the address of the property
        floor_number (int): the floor number of the apartment
        floor_area (int): floor area in m^2 of the property
        price (int): the predicted price of the property
        property_features (list of strings): a list of the features of the property. Could include solar, air conditioning, dishwasher, floorboards, central heating, etc.
        coordinates (tuple of floats): the latitude and longitude of the property
    """
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        floor_number: int,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        """
        Initialises an apartment object.

        Arguments:
            prop_id (str): the property's ID
            bedrooms (int): the number of bedrooms in the property
            bathrooms (int): the number of bathrooms in the property
            parking_spaces (int): the number of car spaces in the property
            full_address (str): the address of the property
            floor_number (int): the floor number of the apartment
            floor_area (int): floor area in m^2 of the property
            price (int): the predicted price of the property
            property_features (list of strings): a list of the features of the property. Could include solar, air conditioning, dishwasher, floorboards, central heating, etc.
            coordinates (tuple of floats): the latitude and longitude of the property
        """
        self.prop_id = prop_id
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.parking_spaces = parking_spaces
        self.full_address = full_address
        self.floor_number = floor_number
        self.floor_area = floor_area
        self.price = price
        self.property_features = property_features
        self.coordinates = coordinates

    def get_floor_number(self) -> int:
        """
        Returns:
            int: the floor number of the apartment
        """
        return self.floor_number
    
    def get_land_area(self) -> None:
        """
        Returns:
            None: as an apartment does not have a land area
        """
        return None

if __name__ == "__main__":
    pass


