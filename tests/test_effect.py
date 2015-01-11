import unittest
import pygame
from seprcph.effect import Effect
from seprcph.event import Event, EventManager
from seprcph.city import City

class TestEffect(unittest.TestCase):

    def setUp(self):
        self.image = pygame.Surface((10, 10))
        self.c = City('London', (50, 50), True, self.image)
        self.ev = Event('ui.clicked', obj=self.c, pos=(100, 100))

    def test_instantiation(self):
        eff = Effect('test_eff', City, lambda x: x, lambda x: x, 2)

    def test_instantiation_invalid_turns(self):
        self.assertRaises(AssertionError, Effect, '', City, lambda x: x, lambda x: x, 0)

    def test_instantiation_border_turns(self):
        eff = Effect('test_eff', City, lambda x: x, lambda x: x, 1)

    def test_apply(self):
        def eff(obj):
            obj.is_capital = False

        effect = Effect('test_eff', City, eff, lambda x: x, 2)
        self.assertTrue(self.c.is_capital)
        EventManager.notify_listeners(self.ev)
        self.assertFalse(self.c.is_capital)
        self.c.is_capital = True

    def test_undo(self):
        def undo(obj):
            obj.name = 'London'

        self.c.name = ''
        effect = Effect('test_eff', City, lambda x: x, undo, 2)
        self.assertEqual(self.c.name, '')
        effect.remove(self.c)
        self.assertEqual(self.c.name, 'London')
