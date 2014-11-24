import unittest

from seprcph import track, player, city

class TestUnlockTrack(unittest.TestCase):
    
    def setUp(self):
        p = player.Player(50, 1)
        c1 = city.City("London", (50, 50), True, None, None)
        c1 = city.City("Birmingham", (50, 50), False, None, None)
        t = track.Track(c1, c2, 0, 10)

    def test_not_enough_gold_player(self):
        t = track.Track(c1, c2, 0, 55)
        self.assertRaises(track.NotEnoughGoldError, t.unlock_track, p)

    def test_track_already_owned(self):
        t.is_locked = False
        self.assertRaises(track.TrackOwnedError, t.unlock_track, p)

    def test_owner_is_changing(self):
        t.unlock_track(p)
        self.assertTrue(t.owner == p)

    def test_is_unlocking(self):
        t.unlock_track(p)
        self.assertTrue(t.is_locked == False)

    def test_gold_updating(self):
        t.unlock_track(p)
        self.assertTrue(p.gold == 40)
