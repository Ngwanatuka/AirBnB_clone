#!/usr/bin/pyhton3
"""
tests the amenity
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test class for the Amenity model
    """

    def setUp(self):
        """
        Method run before each testt to create a new Amenity instance
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Method run after each test to delete the Amenity instance
        """
        del self.amenity

    def test_instance(self):
        """
        Test that an instance of the Amenity model can be created
        """
        self.assertIsInstance(self.amenity, Amenity)

    def test_name_property(self):
        self.amenity.name = "Wi-Fi"
        self.assertEqual(self.amenity.name, "Wi-Fi")

    def test_inheritance(self):
        """
        Test that Amenity model correctly inherits from BaseModel
        """
        self.assertIsInstance(self.amenity, BaseModel)


if __name__ == "__main__":
    unittest.main()
