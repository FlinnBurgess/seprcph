import unittest

from seprcph import goal


class TestCreateGoal(unittest.TestCase):

    def test_negative_reward(self):
        self.assertRaises(AssertionError, goal.Goal, None, [], 1, -1, None)

    def test_negative_turns(self):
        self.assertRaises(AssertionError, goal.Goal, None, [], -1, 1, None)

# TODO: Add tests for completing goals, cities need implementing first though.
