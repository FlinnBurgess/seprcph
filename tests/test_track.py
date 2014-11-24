import unittest

from seprcph import track, player, city

class TestUnlockTrack(unittest.TestCase):

    def setUp(self):
        self.p = player.Player(50, 1, None, None)
        self.c1 = city.City("London", (50, 50), True, None, None)
        self.c2 = city.City("Birmingham", (50, 50), False, None, None)
        self.t = track.Track(self.c1, self.c2, 0, 10)

    def test_not_enough_gold_player(self):
        self.t = track.Track(self.c1, self.c2, 0, 55)
        self.assertRaises(track.NotEnoughGoldError, self.t.unlock_track, self.p)

    def test_track_already_owned(self):
        self.t.is_locked = False
        self.assertRaises(track.TrackOwnedError, self.t.unlock_track, self.p)

    def test_owner_is_changing(self):
        self.t.unlock_track(self.p)
        self.assertEqual(self.t.owner, self.p)

    def test_is_unlocking(self):
        self.t.unlock_track(self.p)
        self.assertEqual(self.t.is_locked, False)

    def test_gold_updating(self):
        self.t.unlock_track(self.p)
        self.assertEqual(self.p.gold, 40)
