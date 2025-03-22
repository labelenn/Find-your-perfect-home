from typing import Tuple, List, Union

class House():
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
        raise NotImplementedError
    # To be implemented

class Apartment():
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
        raise NotImplementedError
    # To be implemented

if __name__ == '__main__':
    pass

