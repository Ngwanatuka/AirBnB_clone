#!/usr/bin/python3
"""this unittest is for the class Place
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """tests the Place class to ensure that it has the expected
    behaviour and attributes.
    """

    def setUp(self):
        """This method creates an instance of the Place class to be used by
        each test method
        """
        self.place = Place()

    def tearDown(self):
        """The method deletes the instances of the Place class created by
        the setUp method to clean up after each test.
        """
        del self.place

    def test_inheritenace(self):
        """Tests that the Place inherits from the BaseModel
        """
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Test the initial values of the Places class atrributes
        """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.max_guests, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
