import unittest

from seprcph import goal, city, player, event


class TestCreateGoal(unittest.TestCase):

    def test_negative_turns(self):
        self.assertRaises(AssertionError, goal.Goal, None, [], -1, 1, 1, None)

    def test_negative_gold_reward(self):
        self.assertRaises(AssertionError, goal.Goal, None, [], 1, -1, 1, None)

    def test_negative_score_reward(self):
        self.assertRaises(AssertionError, goal.Goal, None, [], 1, 1, -1, None)

class TestCompleteGoal(unittest.TestCase):

    def setUp(self):
        self.start_city = city.City('London', (100, 100), False, None, None)
        self.end_city = [city.City('Berlin', (100, 50), False, None, None)]
        self.player = player.Player(0, 0, None, None)
        self.goal = goal.Goal(self.start_city, self.end_city, 4, 100, 100, self.player)

    def test_arrive_at_start_city(self):
        self.assertFalse(self.goal._start_reached)
        event.EventManager.notify_listeners(event.Event('train.arrive', city=self.start_city))
        self.assertTrue(self.goal._start_reached)


# TODO: Add tests for completing goals, cities need implementing first though.
