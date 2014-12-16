import unittest
import pygame

from seprcph.renderable import Renderable

class TestRect (unittest.TestCase):

    def setup(self):
        self.image = pygame.Surface((10, 10))
        self.c = Renderable((50, 50), self.image)

    def test_rect_calc(self):
        self.assertEqual(self.c.pos[0], self.c.rect.centerx)
        self.assertEqual(self.c.pos[1], self.c.rect.centery)
