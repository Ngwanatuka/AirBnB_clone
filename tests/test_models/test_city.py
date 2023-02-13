#!/usr/bin/python3
"""
test case for the city model
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """TestCity class tests the functionality of the City model
    """

    def setUp(self):
        """setUp method sets up the objbects rewuired for the testing
        """
        self.city = City()

    def tearDown(self):
        """tearDown method deletes any existing objects created in the setup
        """
        del self.city

    def test_inheritance(self):
        """test if City class correctly inherits from BaseModel
        """
        self.assertIsInstance(self.city, BaseModel)

    def test_state_id_property(self):
        """tests if the state_id property exists in the City model
        """
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_name_property(self):
        """tests if name propert exists in the City model
        """
        self.assertTrue(hasattr(self.city, "name"))

    def test_state_id_value(self):
        """tests if state_id propert is emppty when is created
        """
        self.assertEqual(self.city.state_id, "")

    def test_name_value(self):
        """tests if name property is empty when object is created
        """
        self.assertEqual(self.city.name, "")


if __name__ == '__main__':
    unittest.main()
