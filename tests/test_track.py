import unittest

import pygame

from seprcph.track import Track, NotEnoughGoldError, TrackOwnedError
from seprcph.player import Player
from seprcph.city import City
from seprcph.deck import Deck
from seprcph.hand import Hand
from seprcph.card import Card

class TestUnlockTrack(unittest.TestCase):

    def setUp(self):
        image = pygame.Surface((10, 10))
        d = Deck(None, [Card('card1', None, None, None, image), Card('card2', None, None, None, image)], None)
        self.p = Player(50, 1, d)
        self.image = pygame.Surface((10, 10))
        self.c1 = City("London", (50, 50), True, self.image)
        self.c2 = City("Birmingham", (50, 50), False, self.image)
        self.t = Track(self.c1, self.c2, 0, 10, self.image)

    def test_not_enough_gold_player(self):
        self.t = Track(self.c1, self.c2, 0, 55, self.image)
        self.assertRaises(NotEnoughGoldError, self.t.unlock_track, self.p)

    def test_track_already_owned(self):
        self.t.is_locked = False
        self.assertRaises(TrackOwnedError, self.t.unlock_track, self.p)

    def test_owner_is_changing(self):
        self.t.unlock_track(self.p)
        self.assertEqual(self.t.owner, self.p)

    def test_is_unlocking(self):
        self.t.unlock_track(self.p)
        self.assertEqual(self.t.is_locked, False)

    def test_gold_updating(self):
        self.t.unlock_track(self.p)
        self.assertEqual(self.p.gold, 40)
