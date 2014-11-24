import unittest

from seprcph import track, player

class TestUnlockTrack(unittest.TestCase):

    def test_not_enough_gold_player(self):
        p = player.Player(10, 1)
        t = track.Track("x", "y", 0, 15)
        self.assertRaises(track.NotEnoughGoldError, t.unlock_track, p)

    def test_track_already_owned(self):
        p = player.Player(50, 1)
        t = track.Track("x", "y", 0, 10)
        t.is_locked = False
        self.assertRaises(track.TrackOwnedError, t.unlock_track, p)

    def test_owner_is_changing(self):
        p = player.Player(50, 1)
        t = track.Track("x", "y", 0, 10)
        t.unlock_track(p)
        self.assertEqual(t.owner, p)

    def test_is_unlocking(self):
        p = player.Player(50, 1)
        t = track.Track("x", "y", 0, 10)
        t.unlock_track(p)
        self.assertEqual(t.is_locked, False)

    def test_gold_updating(self):
        p = player.Player(50, 1)
        t = track.Track("x", "y", 0, 10)
        t.unlock_track(p)
        self.assertEqual(p.gold, 40)
