from typing import Tuple, List, Union
from custom_errors import CustomValueError, CustomTypeError, CustomAttributeError, CustomKeyError

class Amenity():
    """
    Amenity class to represent an amenity object.

    Instance Variables:
        amenity_code (str): the amenity's code
        amenity_name (str): the name of the amenity
        amenity_type (str): the type of the amenity
        amenity_subtype (str): the subtype of the amenity
        coordinates (tuple of floats): the latitude and longitude of the amenity
    """
    def __init__(self, amenity_code: str, 
                        amenity_name: str,
                        amenity_type: str, 
                        amenity_subtype: str,
                        coordinates: Tuple[float, float]):
        """
        Initialises an amenity object.

        Arguments:
            amenity_code (str): the amenity's code
            amenity_name (str): the name of the amenity
            amenity_type (str): the type of the amenity
            amenity_subtype (str): the subtype of the amenity
            coordinates (tuple of floats): the latitude and longitude of the
        """
        self.validate_data(amenity_code, amenity_name, amenity_type, amenity_subtype, coordinates)
        
        self.amenity_code = amenity_code
        self.amenity_name = amenity_name
        self.amenity_type = amenity_type
        self.amenity_subtype = amenity_subtype
        self.amenity_coords = coordinates

    def validate_data(self, amenity_code: str, 
                        amenity_name: str,
                        amenity_type: str, 
                        amenity_subtype: str,
                        coordinates: Tuple[float, float]):
        """
        Validates the data for the amenity object.
        
        Arguments:
            amenity_code (str): the amenity's code
            amenity_name (str): the name of the amenity
            amenity_type (str): the type of the amenity
            amenity_subtype (str): the subtype of the amenity
            coordinates (tuple of floats): the latitude and longitude of the
        """

        if not isinstance(amenity_code, str):
            raise CustomTypeError("Amenity code must be a string")
        if amenity_code in ("", None):
            raise CustomValueError("Amenity code cannot be empty")

        if not isinstance(amenity_name, str):
            raise CustomTypeError("Amenity name must be a string")
        if amenity_name in ("", None):
            raise CustomValueError("Amenity name cannot be empty")

        if not isinstance(amenity_type, str):
            raise CustomTypeError("Amenity type must be a string")
        if amenity_type in ("", None):
            raise CustomValueError("Amenity type cannot be empty")

        if amenity_subtype not in ("", None):
          if not isinstance(amenity_subtype, str):
              raise CustomTypeError("Amenity subtype must be a string")
          
        if not isinstance(coordinates, tuple) or len(coordinates) != 2:
            raise CustomTypeError("Coordinates must be a tuple of two floats")
        if not all(isinstance(coord, float) for coord in coordinates):
            raise CustomTypeError("Coordinates must be a tuple of two floats")

    def get_amenity_code(self) -> str:
        """
        Returns:
            str: the code of the amenity
        """
        return self.amenity_code
    
    def set_amenity_name(self, amenity_name: str) -> None:
        """
        Sets the name of the amenity.

        Arguments:
            amenity_name (str): the name of the amenity
        """
        if not isinstance(amenity_name, str):
            raise CustomTypeError("Amenity name must be a string")
        if amenity_name in ("", None):
            raise CustomValueError("Amenity name cannot be empty")
            
        self.amenity_name = amenity_name
    
    def get_amenity_name(self) -> str:
        """
        Returns:
            str: the name of the amenity
        """
        return self.amenity_name
    
    def get_amenity_coords(self) -> Tuple[float, float]:
        """
        Returns:
            tuple of floats: the latitude and longitude of the amenity
        """
        return self.amenity_coords
    
    def get_amenity_type(self) -> str:
        """
        Returns:
            str: the type of the amenity
        """
        return self.amenity_type
    
    def set_amenity_subtype(self, amenity_subtype: Union[str,None]) -> None:
        """
        Sets the subtype of the amenity.

        Arguments:
            amenity_subtype (str or None): the subtype of the amenity
        """
        if amenity_subtype not in ("", None):
            if not isinstance(amenity_subtype, str):
                raise CustomTypeError("Amenity subtype must be a string")

        self.amenity_subtype = amenity_subtype
    
    def get_amenity_subtype(self) -> Union[str,None]:
        """
        Returns:
            str or None: the subtype of the amenity
        """
        return self.amenity_subtype

if __name__ == "__main__":
    a = Amenity("1001")
    

    

