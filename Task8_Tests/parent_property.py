from abc import ABC, abstractmethod
from typing import Tuple, List, Union
from amenity import Amenity
import math
from custom_errors import CustomValueError, CustomTypeError, CustomAttributeError, CustomKeyError

class Property(ABC):
    """
    Property class for representing a property such as a house or an apartment.

    Instance Variables:
        prop_id (str): the property's ID
        bedrooms (int): the number of bedrooms in the property
        bathrooms (int): the number of bathrooms in the property
        parking_spaces (int): the number of car spaces in the property
        full_address (str): the address of the property
        floor_area (int): floor area in m^2 of the property
        price (int): the predicted price of the property
        property_features (list of strings): a semi-colon separated list of the features of the property. Could include solar, air conditioning, dishwasher, floorboards, central heating, etc.
        coordinates (tuple of floats): the latitude and longitude of the property
    """
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        """
        Creates a property object.

        Arguments:
            prop_id (str): the property's ID
            bedrooms (int): the number of bedrooms in the property
            bathrooms (int): the number of bathrooms in the property
            parking_spaces (int): the number of car spaces in the property
            full_address (str): the address of the property
            floor_area (int): floor area in m^2 of the property
            price (int): the predicted price of the property
            property_features (list of strings): a semi-colon separated list of the features of the property. Could include solar, air conditioning, dishwasher, floorboards, central heating, etc.
            coordinates (tuple of floats): the latitude and longitude of the property
        """
        self.prop_id = prop_id
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.parking_spaces = parking_spaces
        self.full_address = full_address
        self.floor_area = floor_area
        self.price = price
        self.property_features = property_features
        self.coordinates = coordinates
    
    def get_prop_id(self) -> str:
        """"
        Returns:
            str: the property's ID
        """
        return self.prop_id

    def get_full_address(self) -> str:
        """"
        Returns:
            str: the full address of the property
        """
        return self.full_address

    def get_suburb(self) -> str:
        """
        Returns:
            str: the suburb of the property
        """
        return self.full_address.split(" ")[-3]
    
    def get_prop_type(self) -> str:
        """
        Returns:
            str: the type of the property. Will return "apartment" if the property is an apartment, and "house" if the property is a house
        """
        return "apartment" if "/" in self.full_address.split(" ")[0] else "house"
    
    def set_bedrooms(self, bedrooms: int) -> None:
        """
        Sets the number of bedrooms in the property

        Arguments:
            bedrooms (int): the number of bedrooms in the property
        """
        if not isinstance(bedrooms, int):
            raise CustomTypeError("Number of bedrooms must be an integer")
        if bedrooms < 0:
            raise CustomValueError("Number of bedrooms must be a non-negative integer")
        
        self.bedrooms = bedrooms
    
    def get_bedrooms(self) -> int:
        """
        Returns:
            int: the number of bedrooms in the property
        """
        return self.bedrooms
    
    def set_bathrooms(self, bathrooms: int) -> None:
        """"
        Sets the number of bathrooms in the property

        Arguments:
            bathrooms (int): the number of bathrooms in the property
        """
        if not isinstance(bathrooms, int):
            raise CustomTypeError("Number of bathrooms must be an integer")
        if bathrooms < 0:
            raise CustomValueError("Number of bathrooms must be a non-negative integer")
        
        self.bathrooms = bathrooms
    
    def get_bathrooms(self) -> int:
        """
        Returns:
            int: the number of bathrooms in the property
        """
        return self.bathrooms
    
    def set_parking_spaces(self, parking_spaces: int) -> None:
        """
        Sets the number of parking spaces in the property

        Arguments:
            parking_spaces (int): the number of car spaces in the property
        """
        if not isinstance(parking_spaces, int):
            raise CustomTypeError("Number of parking spaces must be an integer")
        if parking_spaces < 0:
            raise CustomValueError("Number of parking spaces must be a non-negative integer")
        
        self.parking_spaces = parking_spaces

    def get_parking_spaces(self) -> int:
        """
        Returns:
            int: the number of parking spaces in the property
        """
        return self.parking_spaces
    
    def get_coordinates(self) -> Tuple[float, float]:
        """
        Returns:
            tuple of floats: the latitude and longitude of the
        """
        return self.coordinates
    
    def set_floor_number(self, floor_number: int) -> None:
        """
        Sets the floor number of the property

        Arguments:
            floor_number (int): the floor number of the property
        """
        if not isinstance(floor_number, int):
            raise CustomTypeError("Floor number must be an integer")
        if floor_number < 0:
            raise CustomValueError("Floor number must be a non-negative integer")
        
        self.floor_number = floor_number

    @abstractmethod
    def get_floor_number(self) -> Union[int,None]:
        """
        Returns:
            int or None: the floor number of the property. Will return None if the property is a house
        """
        return None
    
    def set_land_area(self, land_area: int) -> None:
        """
        Sets the land area of the property

        Arguments:
            land_area (int): the land area of the property
        """
        self.land_area = land_area

    @abstractmethod
    def get_land_area(self) -> Union[int,None]:
        """
        Returns:
            int or None: the land area of the property. Will return None if the property is an apartment
        """
        return None
    
    def set_floor_area(self, floor_area: int) -> None:
        """
        Sets the floor area of the property.

        Arguments:
            floor_area (int): the floor area of the property
        """
        self.floor_area = floor_area
    
    def get_floor_area(self) -> int:
        """
        Returns:
            int: the floor area of the property
        """
        return self.floor_area

    def set_price(self, price: int) -> None:
        """
        Sets the price of the property.

        Arguments:
            price (int): the price of the property
        """
        self.price = price
    
    def get_price(self) -> int:
        """
        Returns:
            int: the price of the property
        """
        return self.price
    
    def set_property_features(self, property_features: List[str]) -> None:
        """
        Sets the property features of the property.

        Arguments:
            property_features (list of strings): a list of the features of the property. Could include solar, air conditioning, dishwasher, floorboards, central heating, etc.
        """
        self.property_features = property_features
    
    def get_property_features(self) -> List[str]:
        """
        Returns:
            list of strings: the property features of the property
        """
        return self.property_features
    
    def add_feature(self, feature: str) -> None:
        """
        Adds a feature to the property.

        Arguments:
            feature (str): the feature to add to the property
        """
        if feature not in self.property_features:
            self.get_property_features().append(feature)

    def remove_feature(self, feature: str) -> None:
        """
        Removes a feature from the property.

        Arguments:
            feature (str): the feature to remove from the property
        """
        if feature in self.property_features:
            self.get_property_features().remove(feature)

    def haversine_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the great circle distance between two points on the earth (specified in decimal degrees).

        Arguments:
            lat1 (float): latitude of the first point
            lon1 (float): longitude of the first point
            lat2 (float): latitude of the second point
            lon2 (float): longitude of the second point

        Returns:
            float: the distance between the two points in kilometers
        """
        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        radius_of_earth = 6371  # Radius of the earth in kilometers.
        distance = radius_of_earth * c

        return distance


    def nearest_amenity(self, amenities: List[Amenity], amenity_type: str, amenity_subtype: str = None) -> Tuple[Amenity, float]:
        """
        Returns the nearest amenity to the property.

        Arguments:
            amenities (list of Amenity): a list of all the amenities
            amenity_type (str): the type of the amenity
            amenity_subtype (str): the subtype of the amenity

        Returns:
            tuple: the nearest amenity of the given type and subtype to the property, and its corresponding distance from the property.
        """
        # Validation checks
        # If the type or subtype doesn"t exist or is invalid, return None
        valid_types = ["medical_centre", "school", "train_station", "sport_facility"]
        valid_subtypes = ["Primary", "Secondary", "Pri/Sec"]

        for a in amenities:
            if a.get_amenity_type() == 'sport_facility':
                valid_subtypes.append(a.get_amenity_subtype())

        if amenity_type not in valid_types:
            return None, None
        
        if amenity_subtype is not None and amenity_subtype not in valid_subtypes:
            return None, None
        
        nearest_amenity = None
        nearest_distance = float("inf")

        # Loop through all amenities
        # If the amenity type matches the input amenity type, check if the amenity subtype matches the input amenity subtype (if there is one).
        # If the amenity subtype matches or there is no amenity subtype, calculate the distance between the property and the amenity.
        for amenity in amenities:
            if amenity.get_amenity_type() == amenity_type:
                if amenity_subtype is None:
                    property_coords = self.get_coordinates()
                    amenity_coords = amenity.get_amenity_coords()
                    distance = self.haversine_distance(property_coords[0], property_coords[1], amenity_coords[0], amenity_coords[1])

                    if distance < nearest_distance:
                        nearest_distance = distance
                        nearest_amenity = amenity
                else:
                    if amenity.get_amenity_subtype() == amenity_subtype:
                        property_coords = self.get_coordinates()
                        amenity_coords = amenity.get_amenity_coords()
                        distance = self.haversine_distance(property_coords[0], property_coords[1], amenity_coords[0], amenity_coords[1])

                        if distance < nearest_distance:
                            nearest_distance = distance
                            nearest_amenity = amenity

                    # If the search is "Pri/Sec", check if the amenity subtype is "Primary" or "Secondary" and ensure that the type is "school"
                    elif amenity_subtype == "Pri/Sec" and amenity.get_amenity_subtype() in ["Primary", "Secondary", "Pri/Sec"] and amenity.get_amenity_type() == "school":
                        property_coords = self.get_coordinates()
                        amenity_coords = amenity.get_amenity_coords()
                        distance = self.haversine_distance(property_coords[0], property_coords[1], amenity_coords[0], amenity_coords[1])

                        if distance < nearest_distance:
                            nearest_distance = distance
                            nearest_amenity = amenity

                    # If the amenity itself is "Pri/Sec", check if the check is "Primary" or "Secondary" or "Pri/Sec" and ensure that the type is "school"
                    elif amenity.get_amenity_subtype() == "Pri/Sec" and amenity_subtype in ["Primary", "Secondary", "Pri/Sec"] and amenity.get_amenity_type() == "school":
                        property_coords = self.get_coordinates()
                        amenity_coords = amenity.get_amenity_coords()
                        distance = self.haversine_distance(property_coords[0], property_coords[1], amenity_coords[0], amenity_coords[1])

                        if distance < nearest_distance:
                            nearest_distance = distance
                            nearest_amenity = amenity
    
        return nearest_amenity, nearest_distance

if __name__ == "__main__":
    pass

