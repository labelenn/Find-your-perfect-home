from typing import Tuple, List, Union

class Amenity():
    def __init__(self, amenity_code: str, 
                        amenity_name: str,
                        amenity_type: str, 
                        amenity_subtype: str,
                        coordinates: Tuple[float, float]):
        '''
        Initialises an amenity object.
        '''
        self.amenity_code = amenity_code
        self.amenity_name = amenity_name
        self.amenity_type = amenity_type
        self.amenity_subtype = amenity_subtype
        self.coordinates = coordinates

    def get_amenity_code(self) -> str:
        '''
        Returns the code of the amenity
        '''
        return self.amenity_code
    
    def set_amenity_name(self, amenity_name: str) -> None:
        '''
        Sets the name of the amenity
        '''
        self.amenity_name = amenity_name
    
    def get_amenity_name(self) -> str:
        '''
        Returns the name of the amenity
        '''
        return self.amenity_name
    
    def get_amenity_coords(self) -> Tuple[float, float]:
        '''
        Returns the coordinates of the amenity
        '''
        return self.coordinates
    
    def get_amenity_type(self) -> str:
        '''
        Returns the type of the amenity
        '''
        return self.amenity_type
    
    def set_amenity_subtype(self, amenity_subtype: Union[str,None]) -> None:
        '''
        Sets the subtype of the amenity
        '''
        self.amenity_subtype = amenity_subtype
    
    def get_amenity_subtype(self) -> Union[str,None]:
        '''
        Returns the subtype of the amenity
        '''
        return self.amenity_subtype

if __name__ == '__main__':
    a = Amenity('1001')
    

    
