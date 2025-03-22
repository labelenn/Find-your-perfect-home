from abc import ABC, abstractmethod
from typing import Tuple, List, Union

class Property(ABC):
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        
        '''
        Initializes the Property object with the following attributes:
        - prop_id <str>: the property's ID
        - bedrooms <int>: the number of bedrooms in the property
        - bathrooms <int>: the number of bathrooms in the property
        - parking_spaces <int>: the number of car spaces in the property
        - full_address <str>: this is the address of the property
          -- if it's a house, it will be in the format of "<street number> <street name> <street type> <suburb> <state code> <postcode>"
          -- if it's an apartment, it will be in the format of "<apartment number>/<street number> <street name> <street type> <suburb> <state code> <postcode>"
        - floor_area <int>: floor area in m^2 of the property
        - price <int>: the predicted price of the property
        - property_features <list of strings>: a semi-colon separated list of the features of the property. Could include solar, air conditioning, dishwasher, floorboards, central heating, etc.
          -- this can have 0 items, and if it does, make an empty list
        - coordinates <tuple of floats>: the latitude and longitude of the property
        '''
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
        ''''
        Returns the property ID
        '''
        return self.prop_id

    def get_full_address(self) -> str:
        ''''
        Returns the full address of the property
        '''
        return self.full_address

    def get_suburb(self) -> str:
        '''
        Returns the suburb of the property
        '''
        return self.full_address.split(' ')[-3]
    
    def get_prop_type(self) -> str:
        '''
        Returns the type of the property
        '''
        return 'apartment' if '/' in self.full_address.split(' ')[0] else 'house'
    
    def set_bedrooms(self, bedrooms: int) -> None:
        '''
        Sets the number of bedrooms in the property
        '''
        self.bedrooms = bedrooms
    
    def get_bedrooms(self) -> int:
        '''
        Returns the number of bedrooms in the property
        '''
        return self.bedrooms
    
    def set_bathrooms(self, bathrooms: int) -> None:
        ''''
        Sets the number of bathrooms in the property
        '''
        self.bathrooms = bathrooms
    
    def get_bathrooms(self) -> int:
        '''
        Returns the number of bathrooms in the property
        '''
        return self.bathrooms
    
    def set_parking_spaces(self, parking_spaces: int) -> None:
        '''
        Sets the number of parking spaces in the property
        '''
        self.parking_spaces = parking_spaces

    def get_parking_spaces(self) -> int:
        '''
        Returns the number of parking spaces in the property
        '''
        return self.parking_spaces
    
    def get_coordinates(self) -> Tuple[float, float]:
        '''
        Returns the coordinates of the property
        '''
        return self.coordinates
    
    def set_floor_number(self, floor_number: int) -> None:
        '''
        Sets the floor number of the property
        '''
        self.floor_number = floor_number

    @abstractmethod
    def get_floor_number(self) -> Union[int,None]:
        '''
        Returns the floor number of the property. Will return None if the property is a house
        '''
        return None
    
    def set_land_area(self, land_area: int) -> None:
        '''
        Sets the land area of the property
        '''
        self.land_area = land_area

    @abstractmethod
    def get_land_area(self) -> Union[int,None]:
        '''
        Returns the land area of the property. Will return None if the property is an apartment
        '''
        return None
    
    def set_floor_area(self, floor_area: int) -> None:
        '''
        Sets the floor area of the property
        '''
        self.floor_area = floor_area
    
    def get_floor_area(self) -> int:
        '''
        Returns the floor area of the property
        '''
        return self.floor_area

    def set_price(self, price: int) -> None:
        '''
        Sets the price of the property
        '''
        self.price = price
    
    def get_price(self) -> int:
        '''
        Returns the price of the property
        '''
        return self.price
    
    def set_property_features(self, property_features: List[str]) -> None:
        '''
        Sets the property features of the property
        '''
        self.property_features = property_features
    
    def get_property_features(self) -> List[str]:
        '''
        Returns the property features of the property
        '''
        return self.property_features

if __name__ == '__main__':
    pass
