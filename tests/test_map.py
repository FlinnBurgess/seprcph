import unittest
import os
import pygame
import platform
import errno
from seprcph.map import Map
from seprcph.track import Track
from seprcph.city import City
from seprcph.config import Config

if platform.system() == 'Windows':
    path = os.path.join(os.getcwd(), 'config.cfg')
else:
    path = os.path.join(os.getcwd(), 'config.cfg')

def setUpModule():
    Config.load_config(path)
    Config.general['data_dir'] = os.path.join(os.getcwd(), 'data')
    Config.general['image_dir'] = os.path.join(os.getcwd(), 'assets', 'images')

def tearDownModule():
    try:
        os.remove(path)
    except OSError as err:
        if err.errno != errno.ENOENT:
            raise


class TestMap(unittest.TestCase):

    def setUp(self):
        self.image = pygame.Surface((10, 10))

    def test_init(self):
        self.map = Map(self.image)
        self.assertIsInstance(self.map, Map)

class TestFetchAndAdd(unittest.TestCase):

    def setUp(self):
        self.image = pygame.Surface((10, 10))
        self.map = Map(self.image)
        self.first_city = self.map._cities.keys()[0]
        self.second_city = self.map._cities.keys()[1]
        self.test_track = Track(self.first_city, self.second_city, 5, 10, self.image)

    def test_fetching_indices(self):
        self.assertEqual(self.map.fetch_indices((self.first_city, self.second_city)), (0, 1))

    def test_add_track(self):
        self.map.add_track(self.test_track)
        self.assertEqual(self.map._matrix[0][1], self.test_track)

    def test_fetch_track(self):
        self.map.add_track(self.test_track)
        self.assertEqual(self.map.fetch_track((self.first_city, self.second_city)), self.test_track)
