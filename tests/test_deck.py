import unittest, random, pygame

from seprcph.deck import Deck
from seprcph.card import Card

class TestDeckMethods(unittest.TestCase):
    def setUp(self):
        image = pygame.Surface((10, 10))
        self.test_card = Card("test", 1, None, None, image)
        self.deck = Deck(None, [self.test_card], None)

    def test_deck_pop(self):
        self.assertEqual(self.deck.pop(), self.test_card)

    def test_add_to_discard(self):
        self.deck.add_to_discard(self.test_card)
        self.assertEqual(self.deck.discard.pop(), self.test_card)

    def test_restart(self):
        self.deck.cards = []
        self.deck.discard = [self.test_card]
        self.deck.restart()
        self.assertEqual(self.deck.discard, [])