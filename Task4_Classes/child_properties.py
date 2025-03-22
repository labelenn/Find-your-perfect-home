from typing import Tuple, List, Union
from parent_property import Property

class House(Property):
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
        '''
        Initialises a house object.
        '''
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
        '''
        Returns the land area of the property
        '''
        return self.land_area

class Apartment(Property):
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
        '''
        Initialises an apartment object.
        '''
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
        '''
        Returns the floor number of the property
        '''
        return self.floor_number

if __name__ == '__main__':
    pass

