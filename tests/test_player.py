import unittest

from seprcph.player import Player


class TestCreatePlayer(unittest.TestCase):

    def test_no_deck(self):
        self.assertRaises(AssertionError, Player, 0, 0, None)

