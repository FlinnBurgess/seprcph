import unittest
import pygame
from seprcph.effect import Effect, Affectable
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
        effect.apply(Event('ui.select_effect', obj=self.c))
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


class TestAffectable(unittest.TestCase):

    def setUp(self):
        self.aff = Affectable()

    def test_add_effect(self):
        self.aff.add_effect(Effect('test_Eff', City, lambda x: x, lambda x: x, 2))
        self.assertEqual(1, len(self.aff.effects))

    def test_decrement_turns(self):
        self.aff.add_effect(Effect('test_Eff', City, lambda x: x, lambda x: x, 2))
        self.aff.decrement_turns()
        self.assertEqual(1, self.aff.effects[0].turns)

    def test_remove_effect(self):
        self.aff.add_effect(Effect('test_Eff', City, lambda x: x, lambda x: x, 1))
        self.aff.decrement_turns()
        self.assertEqual(0, len(self.aff.effects))
