import unittest

from seprcph.card import Card
from seprcph.deck import Deck, Hand

class TestCreateCard(unittest.TestCase):

    def test_no_desc_card(self):
        c = Card('name', 123, '', 'An effect', 'filename.jpg')
        self.assertEqual(c.desc, '')

    def test_no_effect_card(self):
        c = Card('name', 123, 'A description', '', 'filename.jpg')
        self.assertEqual(c.effect, '')

    def test_no_image_card(self):
        c = Card('name', 123, 'A description', 'An effect', '')
        self.asserEqual(c.image, '')


