__author__ = 'Ethan'

import unittest

import pygame

from seprcph.city import City

class TestCityArgs (unittest.TestCase):

    def setup(self):
        self.image = pygame.Surface((10, 10))
        self.c1 = City("London", (50, 50), True, self.image)
        self.c2 = City("Paris", (120, 30), True, self.image)

    def test_occupy_dif_pos(self):
        self.assertNotEqual(self.c1.pos, self.c2.pos)

    def test_is_capital_type(self):
        self.assertIsInstance(self.c1.is_capital, bool)

    def test_dif_names(self):
        self.assertNotEqual(self.c1.name, self.c2.name)

class TestCityRect (unittest.TestCase):

    def setup(self):
        self.image = pygame.Surface((10, 10))
        self.c = City("London", (50, 50), True, self.image)

    def test_rect_calc(self):
        self.assertEqual(self.c.pos[0], self.c.rect.centerx)
        self.assertEqual(self.c.pos[1], self.c.rect.centery)
