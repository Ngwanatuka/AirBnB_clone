#!/usr/bin/python3
"""Test case for the State model
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestStateModel(unittest.TestCase):
    """Test class for state model"""

    def setUp(self):
        """Creat an instance of the State model before each test"""
        self.state = State()

    def tearDown(self):
        """Delete the State instance after each test"""
        del self.state

    def test_name_attribute(self):
        """Test if the name attribute of the State class is correctly
        initialized and if it can be modified"""
        self.assertEqual(self.state.name, "")
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")


if __name__ == '__main__':
    unittest.main()
