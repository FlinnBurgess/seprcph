import unittest

import pygame

from seprcph.track_matrix import TrackMatrix
from seprcph.track import Track
from seprcph.city import City

class TestFetchAndAdd(unittest.TestCase):

    def setUp(self):
        self.adj_matrix = TrackMatrix(["london", "cardiff"])
        self.london = City("london", (100, 100), True, None)
        self.cardiff = City("cardiff", (200, 200), True, None)
        self.pos = ((self.london.pos[0] + self.cardiff.pos[0]) / 2,
                    (self.london.pos[1] + self.cardiff.pos[1]) / 2)
        self.image = pygame.Surface((10, 10))
        self.test_track = Track(self.london, self.cardiff, 5, 10, self.pos, self.image)

    def test_fetching_indices(self):
        self.assertEqual(self.adj_matrix.fetch_indices((self.london, self.cardiff)), (0, 1))

    def test_add_track(self):
        self.adj_matrix.add_track((self.london, self.cardiff), 5, 10, self.pos, self.image)
        self.assertEqual(self.adj_matrix._matrix[0][1], self.test_track)

    def test_fetch_track(self):
        self.adj_matrix._matrix[0][1] = Track(self.london, self.cardiff, 5, 10, self.pos, self.image)
        self.assertEqual(self.adj_matrix.fetch_track((self.london, self.cardiff)), self.test_track)