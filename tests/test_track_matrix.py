import unittest

from seprcph.track_matrix import TrackMatrix
from seprcph.track import Track 
from seprcph.city import City

class TestFetchAndAdd(unittest.TestCase):

    def setUp(self):
        self.adj_matrix = TrackMatrix(["london", "cardiff"])
        self.london = City("london", None, True, None)
        self.cardiff = City("cardiff", None, True, None)
        self.test_track = Track(self.london, self.cardiff, 5, 10)

    def test_fetching_indices(self):
        self.assertEqual(self.adj_matrix.fetch_indices((self.london, self.cardiff)), (0, 1))

    def test_add_track(self):
        self.adj_matrix.add_track((self.london, self.cardiff), 5, 10)
        self.assertEqual(self.adj_matrix._matrix[0][1], self.test_track)

    def test_fetch_track(self):
        self.adj_matrix._matrix[0][1] = Track(self.london, self.cardiff, 5, 10)
        self.assertEqual(self.adj_matrix.fetch_track((self.london, self.cardiff)), self.test_track)
