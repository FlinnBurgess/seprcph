import unittest

from seprcph import track_matrix, track, city

class TestFetchAndAdd(unittest.TestCase):

    def setUp(self):
        self.adj_matrix = track_matrix.TrackMatrix(["london", "cardiff"])
        self.london = city.City("london", None, True, None, None)
        #NEEDS CHANGING ONCE THE UPDATE TO RECT IS MADE
        self.cardiff = city.City("cardiff", None, True, None, None)
        self.test_track = track.Track(self.london, self.cardiff, 5, 10)

    def test_fetching_indices(self):
        self.assertEqual(self.adj_matrix.fetch_indices((self.london, self.cardiff)), (0, 1))

    def test_add_track(self):
        self.adj_matrix.add_track((self.london, self.cardiff), 5, 10)
        self.assertEqual(self.adj_matrix._matrix[0][1], self.test_track)

    def test_fetch_track(self):
        self.adj_matrix._matrix[0][1] = track.Track(self.london, self.cardiff, 5, 10)
        self.assertEqual(self.adj_matrix.fetch_track((self.london, self.cardiff)), self.test_track)