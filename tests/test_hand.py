import unittest, random

from seprcph.deck import Deck 
from seprcph.hand import Hand
from seprcph.card import Card

x = 0
def _func():
    global x
    x = 1

class TestHandMethods(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("card1", None, None, None, None)
        self.card2 = Card("card2", None, None, None, None)
        self.card3 = Card("card3", None, None, None, None)
        self.card4 = Card("card4", None, None, None, None)
        self.card5 = Card("card5", None, None, _func(), None)
        self.deck = Deck(None, [self.card1, self.card2, self.card3,
                                self.card4], None)
        self.hand = Hand([self.card5], self.deck)

    def test_draw_cards(self):
        self.hand.draw_cards(2)
        self.assertEqual(self.hand.cards, [self.card5, self.card4, self.card3])

    def test_discard(self):
        self.hand.discard(0)
        self.assertEqual(self.hand.deck.discard, [self.card5])
        
    def test_play(self):
        self.hand.play(0)
        self.assertEqual(x, 1)
