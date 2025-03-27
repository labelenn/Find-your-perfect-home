from abc import ABC, abstractmethod
from typing import Tuple, List, Union

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

if __name__ == "__main__":
    pass
