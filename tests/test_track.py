import unittest

from seprcph.track import Track, NotEnoughGoldError, TrackOwnedError
from seprcph.player import Player
from seprcph.city import City

class TestUnlockTrack(unittest.TestCase):

    def setUp(self):
        self.p = Player(50, 1, None, None)
        self.c1 = City("London", (50, 50), True, None, None)
        self.c2 = City("Birmingham", (50, 50), False, None, None)
        self.t = Track(self.c1, self.c2, 0, 10)

    def test_not_enough_gold_player(self):
        self.t = Track(self.c1, self.c2, 0, 55)
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
