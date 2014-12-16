__author__ = 'Ethan'

import unittest

import pygame

from seprcph.city import City

class TestCityRect (unittest.TestCase):

    def setup(self):
        self.image = pygame.Surface((10, 10))
        self.c = City("London", (50, 50), True, self.image)
        
    def test_rect_calc(self):
        self.assertEqual(self.c.pos[0], self.c.rect.centerx)
        self.assertEqual(self.c.pos[1], self.c.rect.centery)