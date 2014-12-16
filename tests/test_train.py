import unittest, pygame
from seprcph.train import Train
from seprcph.city import City
from seprcph.track import Track


class TestCreateTrain(unittest.TestCase):

    def test_no_image_train(self):
        image = pygame.Surface((10,10))
        self.assertRaises(AttributeError, Train, [], [], 2, 1, City('London', (12,13), True, image), None)

    def test_negative_speed(self):
        image = pygame.Surface((10,10))
        self.assertRaises(AssertionError, Train, [], [], -1, 1, City('London', (12,13), True, image), image)

    def test_negative_capacity(self):
        image = pygame.Surface((10,10))
        self.assertRaises(AssertionError, Train, [], [], 2, -1, City('London', (12,13), True, image), image)

class TestDepart(unittest.TestCase):

    def setUp(self):
        image = pygame.Surface((10,10))
        self.city1 = City('London', (12,13), True, image)
        self.city2 = City('York', (15,13), False, image)
        self.train = Train([], [], 2, 1, self.city1, image)
        self.test_track = Track(self.city1, self.city2, 1, 5, image)

    def test_speed_not_zero(self):
        self.assertNotEqual(self.train.speed, 0)

    def test_city_reached(self):
        t = self.train
        t.depart(self.test_track)
        t.arrive(self.city2)
        self.assertEqual(t.city, self.test_track.end_city)

    def test_correct_track(self):
        t = self.train
        t.depart(self.test_track)
        self.assertEqual(t.track, self.test_track)

