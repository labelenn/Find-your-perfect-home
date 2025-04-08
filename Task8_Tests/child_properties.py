from typing import Tuple, List, Union
from parent_property import Property
from custom_errors import CustomValueError, CustomTypeError, CustomAttributeError, CustomKeyError

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

        self.validate_data(prop_id, bedrooms, bathrooms, parking_spaces, full_address, land_area, floor_area, price, property_features, coordinates)
            
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
        self.suburb = full_address.split(" ")[-3]

    def validate_data(self, prop_id: str, 
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
        Validates the data for the house object.

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

        if not isinstance(prop_id, str):
            raise CustomTypeError("Property ID must be a string")
        if prop_id in ("", None):
            raise CustomValueError("Property ID cannot be empty")

        if not isinstance(bedrooms, int):
            raise CustomTypeError("Number of bedrooms must be an integer")
        if bedrooms < 0:
            raise CustomValueError("Number of bedrooms must be a non-negative integer")
        
        if not isinstance(bathrooms, int):
            raise CustomTypeError("Number of bathrooms must be an integer")
        if bathrooms < 0:
            raise CustomValueError("Number of bathrooms must be a non-negative integer")

        if not isinstance(parking_spaces, int):
            raise CustomTypeError("Number of parking spaces must be an integer")
        if parking_spaces < 0:
            raise CustomValueError("Number of parking spaces must be a non-negative integer")
        
        # The house address is in this format:
        # <street number> <street name> <street type> <suburb> <state code> <postcode>
        if not isinstance(full_address, str):
            raise CustomTypeError("Full address must be a string")
        if full_address in ("", None):
            raise CustomValueError("Full address cannot be empty")
        if len(full_address.split(" ")) != 6:
            raise CustomValueError("Full address is not valid. It must be in the format <street number> <street name> <street type> <suburb> <state code> <postcode>")
        if full_address.split(" ")[0].isdigit() == False:
            raise CustomValueError("Street/house number must be a proper number")
        if full_address.split(" ")[5].isdigit() == False:
            raise CustomValueError("Postcode must be a proper number")

        if not isinstance(land_area, int):
            raise CustomTypeError("Land area must be an integer")
        if land_area < 0:
            raise CustomValueError("Land area must be a non-negative integer")
        
        if not isinstance(floor_area, int):
            raise CustomTypeError("Floor area must be an integer")
        if floor_area < 0:
            raise CustomValueError("Floor area must be a non-negative integer")
        
        if not isinstance(price, int):
            raise CustomTypeError("Price must be an integer")
        if price < 0:
            raise CustomValueError("Price must be a non-negative integer")
        
        if property_features is not None:
          if not isinstance(property_features, list):
              raise CustomTypeError("Property features must be a list of strings")
          for feature in property_features:
              if not isinstance(feature, str):
                  raise CustomTypeError("Each property feature must be a string")
        
        if not isinstance(coordinates, tuple) or len(coordinates) != 2:
            raise CustomTypeError("Coordinates must be a tuple of two floats")

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
       
        self.validate_data(prop_id, bedrooms, bathrooms, parking_spaces, full_address, floor_number, floor_area, price, property_features, coordinates)

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
        self.suburb = full_address.split(" ")[-3]

    def validate_data(self, prop_id: str,
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
        Validates the data for the apartment object.

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

        if not isinstance(prop_id, str):
            raise CustomTypeError("Property ID must be a string")
        if prop_id in ("", None):
            raise CustomValueError("Property ID cannot be empty")

        if not isinstance(bedrooms, int):
            raise CustomTypeError("Number of bedrooms must be an integer")
        if bedrooms < 0:
            raise CustomValueError("Number of bedrooms must be a non-negative integer")
        if not isinstance(bathrooms, int):
            raise CustomTypeError("Number of bathrooms must be an integer")
        if bathrooms < 0:
            raise CustomValueError("Number of bathrooms must be a non-negative integer")
        
        if not isinstance(parking_spaces, int):
            raise CustomTypeError("Number of parking spaces must be an integer")
        if parking_spaces < 0:
            raise CustomValueError("Number of parking spaces must be a non-negative integer")
        
        # The apartment address is in this format:
        # <apartment number>/<street number> <street name> <street type> <suburb> <state code> <postcode>
        if not isinstance(full_address, str):
            raise CustomTypeError("Full address must be a string")
        if full_address in ("", None):
            raise CustomValueError("Full address cannot be empty")
        if len(full_address.split(" ")) != 6:
            raise CustomValueError("Full address is not valid. It must be in the format <apartment number>/<street number> <street name> <street type> <suburb> <state code> <postcode>")
        if full_address.split(" ")[5].isdigit() == False:
            raise CustomValueError("Postcode must be a proper number")

        if not isinstance(floor_number, int):
            raise CustomTypeError("Floor number must be an integer")
        if floor_number < 0:
            raise CustomValueError("Floor number must be a non-negative integer")
        
        if not isinstance(floor_area, int):
            raise CustomTypeError("Floor area must be an integer")
        if floor_area < 0:
            raise CustomValueError("Floor area must be a non-negative integer")
        
        if not isinstance(price, int):
            raise CustomTypeError("Price must be an integer")
        if price < 0:
            raise CustomValueError("Price must be a non-negative integer")
        
        if property_features is not None:
          if not isinstance(property_features, list):
              raise CustomTypeError("Property features must be a list of strings")
          for feature in property_features:
              if not isinstance(feature, str):
                  raise CustomTypeError("Each property feature must be a string")
        
        if not isinstance(coordinates, tuple) or len(coordinates) != 2:
            raise CustomTypeError("Coordinates must be a tuple of two floats")

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


