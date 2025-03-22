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
        raise NotImplementedError
    
    def get_prop_id(self) -> str:
        raise NotImplementedError

    def get_full_address(self) -> str:
        raise NotImplementedError

    def get_suburb(self) -> str:
        raise NotImplementedError
    
    def get_prop_type(self) -> str:
        raise NotImplementedError
    
    def set_bedrooms(self, bedrooms: int) -> None:
        raise NotImplementedError
    
    def get_bedrooms(self) -> int:
        raise NotImplementedError
    
    def set_bathrooms(self, bathrooms: int) -> None:
        raise NotImplementedError
    
    def get_bathrooms(self) -> int:
        raise NotImplementedError
    
    def set_parking_spaces(self, parking_spaces: int) -> None:
        raise NotImplementedError

    def get_parking_spaces(self) -> int:
        raise NotImplementedError
    
    def get_coordinates(self) -> Tuple[float, float]:
        raise NotImplementedError
    
    def set_floor_number(self, floor_number: int) -> None:
        raise NotImplementedError

    def get_floor_number(self) -> Union[int,None]:
        raise NotImplementedError
    
    def set_land_area(self, land_area: int) -> None:
        raise NotImplementedError

    def get_land_area(self) -> Union[int,None]:
        raise NotImplementedError
    
    def set_floor_area(self, floor_area: int) -> None:
        raise NotImplementedError
    
    def get_floor_area(self) -> int:
        raise NotImplementedError

    def set_price(self, price: int) -> None:
        raise NotImplementedError
    
    def get_price(self) -> int:
        raise NotImplementedError
    
    def set_property_features(self, property_features: List[str]) -> None:
        raise NotImplementedError
    
    def get_property_features(self) -> List[str]:
        raise NotImplementedError

if __name__ == '__main__':
    pass
