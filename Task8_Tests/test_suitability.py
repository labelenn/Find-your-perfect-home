import unittest
from task8 import find_matching_properties, create_response_dict
from ingestion import ingest_files


class TestSuitability(unittest.TestCase):
    def test_find_matching_properties_return_type(self):
        house_importance = {'suburb': 'Clayton', 'prop_type': 'apartment', 'bedrooms': 3,
                            'bathrooms': 2, 'parking_spaces': 1, 'price': 900000,
                            'property_features': 'air conditioning'}
        props, amens = ingest_files('melbourne_properties.csv', 'melbourne_medical.csv',
                                    'melbourne_schools.csv', 'train_stations.csv', 'sport_facilities.csv')

        matched_props = find_matching_properties(props, house_importance)

        # Check that the returned item is a list
        self.assertEqual(type(matched_props), type(
            []), f"Expected a list to be returned, got a {type(matched_props)} instead")


if __name__ == '__main__':
    unittest.main()

