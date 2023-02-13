#!/usr/bin/python3
"""This a Unittest model for User"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """This test case for the Uder model class"""
    def setUp(self):
        """Sets up the user instance for testing"""
        self.user = User()

    def tearDown(self):
        """Removes the user instance after testing"""
        del self.user

    def test_user_inheritance(self):
        """Tests if the User class correctly
        inherits from BaseMode
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes(self):
        """Tests if the User calss has the correct
        default attribute values
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()
