from typing import Tuple, List, Union

class Amenity():
    def __init__(self, amenity_code: str, 
                        amenity_name: str,
                        amenity_type: str, 
                        amenity_subtype: str,
                        coordinates: Tuple[float, float]):
        raise NotImplementedError

    def get_amenity_code(self) -> str:
        raise NotImplementedError
    
    def set_amenity_name(self, amenity_name: str) -> None:
        raise NotImplementedError
    
    def get_amenity_name(self) -> str:
        raise NotImplementedError
    
    def get_amenity_coords(self) -> Tuple[float, float]:
        raise NotImplementedError
    
    def get_amenity_type(self) -> str:
        raise NotImplementedError
    
    def set_amenity_subtype(self, amenity_subtype: Union[str,None]) -> None:
        raise NotImplementedError
    
    def get_amenity_subtype(self) -> Union[str,None]:
        raise NotImplementedError

if __name__ == '__main__':
    a = Amenity('1001')
    

    
