import unittest

from seprcph.player import Player
from seprcph.hand import Hand
from seprcph.card import Card
from seprcph.deck import Deck


class TestCreatePlayer(unittest.TestCase):

    def test_no_deck(self):
        d = Deck('Moriarty', [], None)
        h = Hand([], d)
        p = Player(23, 2, None, h)
        self.assertIsNone(p.deck)

    def test_no_hand(self):
        d = Deck('Moriarty', [], None)
        p = Player(23, 2, d, None)
        self.assertIsNone(p.hand)


