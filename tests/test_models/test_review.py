#!/usr/bin/python3
"""this unittest if for the model Review
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Unit test for the Riview class
    """

    def setUp(self):
        """Set up the metho to create an instance of the
         Review class for each test
        """
        self.review = Review()

    def test_review_inherits_from_base_model(self):
        """Test if revview class inherits from BaseModel
        """
        self.assertTrue(hasattr(self.review, "place_id"))

    def test_review_has_attribute_text(self):
        """Test if Review class has attribute text
        """
        self.assertTrue(hasattr(self.review, "text"))


if __name__ == '__main__':
    unittest.main()
