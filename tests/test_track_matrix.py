import unittest

import pygame

from seprcph.track_matrix import TrackMatrix
from seprcph.track import Track
from seprcph.city import City

class TestFetchAndAdd(unittest.TestCase):

    def setUp(self):
        self.image = pygame.Surface((10, 10))
        self.london = City("london", (100, 100), True, self.image)
        self.cardiff = City("cardiff", (200, 200), True, self.image)
        self.test_track = Track(self.london, self.cardiff, 5, 10, self.image)
        self.adj_matrix = TrackMatrix([self.london, self.cardiff], [self.test_track])

    def test_fetching_indices(self):
        self.assertEqual(self.adj_matrix.fetch_indices((self.london, self.cardiff)), (0, 1))

    def test_add_track(self):
        self.adj_matrix.add_track(self.test_track)
        self.assertEqual(self.adj_matrix._matrix[0][1], self.test_track)

    def test_fetch_track(self):
        self.adj_matrix.add_track(self.test_track)
        self.assertEqual(self.adj_matrix.fetch_track((self.london, self.cardiff)), self.test_track)
