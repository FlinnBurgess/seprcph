import unittest
import pygame

from seprcph.map import Map
from seprcph.track import Track
from seprcph.city import City

class TestMap(unittest.TestCase):

    def setUp(self):
        self.image = pygame.Surface((10, 10))
        london = City("london", (100, 100), True, None)
        cardiff = City("cardiff", (200, 200), True, None)
        self.cities = [london, cardiff]
        self.tracks = [Track(london, cardiff, 5, 10, self.image)]

    def test_init(self):
        self.map = Map(self.cities, self.tracks, self.image)
        self.assertIsInstance(self.map, Map)
