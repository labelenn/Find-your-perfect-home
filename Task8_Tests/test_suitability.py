import unittest
from task8 import find_matching_properties, create_response_dict
from ingestion import ingest_files
from parent_property import Property


class TestSuitability(unittest.TestCase):
    def test_find_matching_properties_return_type(self):
        """
        This test checks that the find_matching_properties function returns a list.
        """
        
        house_importance = {'suburb': 'Clayton', 'prop_type': 'apartment', 'bedrooms': 3,
                            'bathrooms': 2, 'parking_spaces': 1, 'price': 900000,
                            'property_features': 'air conditioning'}
        props, amens = ingest_files('melbourne_properties.csv', 'melbourne_medical.csv',
                                    'melbourne_schools.csv', 'train_stations.csv', 'sport_facilities.csv')

        matched_props = find_matching_properties(props, house_importance)

        # Check that the returned item is a list
        self.assertEqual(type(matched_props), type(
            []), f"Expected a list to be returned, got a {type(matched_props)} instead")
        
    def test_find_matching_properties_returned_items_type(self):
        """
        This test checks that the find_matching_properties function returns a list of Property objects.
        """

        house_importance = {'suburb': 'Clayton', 'prop_type': 'apartment', 'bedrooms': 3,
                            'bathrooms': 2, 'parking_spaces': 1, 'price': 900000,
                            'property_features': 'air conditioning'}
        props, amens = ingest_files('melbourne_properties.csv', 'melbourne_medical.csv',
                                    'melbourne_schools.csv', 'train_stations.csv', 'sport_facilities.csv')

        matched_props = find_matching_properties(props, house_importance)

        # Check that the returned items are of type Property
        for prop in matched_props:
            self.assertEqual(type(prop), Property,
                             f"Expected a Property object, got {type(prop)} instead")
            
    def test_find_matching_properties_returned_items_count(self):
        """
        This test checks that the find_matching_properties function returns one matching property based on the given house importance.
        """

        house_importance = {'suburb': 'Clayton', 'prop_type': 'apartment', 'bedrooms': 3,
                            'bathrooms': 2, 'parking_spaces': 1, 'price': 900000,
                            'property_features': 'air conditioning'}
        props, amens = ingest_files('melbourne_properties.csv', 'melbourne_medical.csv',
                                    'melbourne_schools.csv', 'train_stations.csv', 'sport_facilities.csv')

        matched_props = find_matching_properties(props, house_importance)

        # Check that the returned items count is correct
        self.assertEqual(len(matched_props), 1,
                         f"Expected 1 matching property, got {len(matched_props)} instead")
        
    def test_create_response_dict_return_type(self):
        """
        This test checks that the create_response_dict function returns a dictionary.
        """

        scored_properties = {'5': Property('5', 'Clayton', 'apartment', 3, 2, 1, 900000, ['air conditioning'], (37.9, 145.1), 4.5)}
        response_dict = create_response_dict(scored_properties)

        # Check that the returned item is a dictionary
        self.assertEqual(type(response_dict), dict,
                         f"Expected a dictionary to be returned, got a {type(response_dict)} instead")
        
    def test_create_response_dict_returned_dict_key(self):
        """
        This test checks that the create_response_dict function returns a dictionary with properties key.
        """

        scored_properties = {'5': Property('5', 'Clayton', 'apartment', 3, 2, 1, 900000, ['air conditioning'], (37.9, 145.1), 4.5)}
        response_dict = create_response_dict(scored_properties)

        # Check that the returned dictionary returned contains 'properties' key
        self.assertIn('properties', response_dict,
                      f"Expected 'properties' key in the returned dictionary, got {response_dict.keys()} instead")
        
    def test_create_response_dict_returned_dict_value(self):
        """
        This test checks that the create_response_dict function returns a dictionary with properties key containing a list.
        """
        scored_properties = {'5': Property('5', 'Clayton', 'apartment', 3, 2, 1, 900000, ['air conditioning'], (37.9, 145.1), 4.5)}
        response_dict = create_response_dict(scored_properties)

        # Check that the returned dictionary returned contains a list of dictionaries
        self.assertEqual(type(response_dict['properties']), list,
                         f"Expected a list to be returned in 'properties' key, got {type(response_dict['properties'])} instead")


if __name__ == '__main__':
    unittest.main()

