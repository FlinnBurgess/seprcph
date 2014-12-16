import unittest

from seprcph.card import Card

class TestCreateCard(unittest.TestCase):

    def test_no_image_card(self):
        self.assertRaises(AssertionError, Card, None, 'A name', 123, 'A description', 'An effect', None)


