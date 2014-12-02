import unittest, random

from seprcph.deck import Deck, Hand
from seprcph.card import Card

class TestHandMethods(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("card1", None, None, None, None)
        self.card2 = Card("card2", None, None, None, None)
        self.card3 = Card("card3", None, None, None, None)
        self.card4 = Card("card4", None, None, None, None)
        self.card5 = Card("card4", None, None, None, None)
        self.deck = Deck(None, [self.card1, self.card2, self.card3,
                                self.card4], None)
        self.hand = Hand([], self.deck)

    def test_draw_cards(self):
        self.hand.draw_cards(2)
        self.assertEqual(self.hand.cards, [self.card4, self.card3])

    def test_discard(self):
        self.hand = Hand([self.card5], self.deck)
        self.hand.discard(0)
        self.assertEqual(self.hand.deck.discard, [self.card5])