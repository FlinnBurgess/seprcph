import unittest

from seprcph.card import Card

class TestCreateCard(unittest.TestCase):

    def test_no_image_card(self):
        self.assertRaises(AttributeError, Card, None, 'A name',
                        'A description', 'An effect', (0, 0), None)
