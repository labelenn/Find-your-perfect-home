from typing import Tuple, List, Union

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
        self.amenity_code = amenity_code
        self.amenity_name = amenity_name
        self.amenity_type = amenity_type
        self.amenity_subtype = amenity_subtype
        self.coordinates = coordinates

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
        return self.coordinates
    
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
        self.amenity_subtype = amenity_subtype
    
    def get_amenity_subtype(self) -> Union[str,None]:
        """
        Returns:
            str or None: the subtype of the amenity
        """
        return self.amenity_subtype

if __name__ == "__main__":
    a = Amenity("1001")
    

    
