import unittest
import os
import pygame
from seprcph.map import Map
from seprcph.track import Track
from seprcph.city import City
from seprcph.config import Config

class TestMap(unittest.TestCase):

    def setUp(self):
        Config.general['data_dir'] = os.path.join(os.getcwd(), 'data')
        Config.general['image_dir'] = os.path.join(os.getcwd(), 'assets', 'images')
        self.image = pygame.Surface((10, 10))

    def test_init(self):
        self.map = Map(self.image)
        self.assertIsInstance(self.map, Map)
