import unittest
import pygame
from seprcph.renderable import Renderable

class TestRect(unittest.TestCase):

    def setUp(self):
        self.image = pygame.Surface((10, 10))
        self.render = Renderable((50, 50), self.image)

    def test_rect_calc(self):
        self.assertEqual(self.render.pos[0], self.render.rect.centerx)
        self.assertEqual(self.render.pos[1], self.render.rect.centery)
