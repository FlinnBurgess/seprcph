import unittest

from seprcph import track_matrix, track, city

class TestFetchAndAdd(unittest.TestCase):

    def setUp(self):
        self.matrix = track_matrix.TrackMatrix(["london", "cardiff"])
        self.london = city.City("london", None, True, None, None)
        #NEEDS CHANGING ONCE THE UPDATE TO RECT IS MADE
        self.cardiff = city.City("cardiff", None, True, None, None)

    def test_fetching_indices(self):
        self.assertEqual(self.matrix.fetch_indices((self.london, self.cardiff)), (0, 1))