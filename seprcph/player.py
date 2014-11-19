__author__ = 'Flinn'
import unittest

class Player():
    """
    Player class that represents each player.

    Args:
        gold: The amount of gold the player currently has
        score: The player's current score

    Raises:
        Fuk knows m8
        AM I EVEN DOING THIS RIGHT
    """

    def __init__(self, gold, score):

        """
        :type gold: int
        :type score: int
        """

        self.gold = gold
        self.score = score

    def update(self):
        """
        This handles the updating of any attributes of an instance of Player

        """
        # self.gold += gold_generation
        # self.score += score_gained