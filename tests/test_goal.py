import unittest
import pygame
from seprcph.goal import Goal
from seprcph.city import City
from seprcph.player import Player
from seprcph.event import Event, EventManager


class TestCreateGoal(unittest.TestCase):

    def test_negative_turns(self):
        self.assertRaises(AssertionError, Goal, None, [], -1, 1, 1, None)

    def test_negative_gold_reward(self):
        self.assertRaises(AssertionError, Goal, None, [], 1, -1, 1, None)

    def test_negative_score_reward(self):
        self.assertRaises(AssertionError, Goal, None, [], 1, 1, -1, None)

class TestCompleteGoal(unittest.TestCase):

    def setUp(self):
        image = pygame.Surface((10, 10))
        self.start_city = City('London', (100, 100), False, image)
        self.end_city = [City('Berlin', (100, 50), False, image)]
        self.player = Player(0, 0, None, None)
        self.goal = Goal(self.start_city, self.end_city, 4, 100, 100, self.player)

    def test_arrive_at_start_city(self):
        self.assertFalse(self.goal._start_reached)
        EventManager.notify_listeners(Event('train.arrive', city=self.start_city))
        self.assertTrue(self.goal._start_reached)


# TODO: Add tests for completing goals, cities need implementing first though.
