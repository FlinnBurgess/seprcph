__author__ = 'Flinn'
"""
This module contains all classes relating to the player.

NAME
    player

FILE
    seprcph/player.py

CLASSES
    Player
"""


class Player(object):
    """
    Player class that represents each player.
    """

    def __init__(self, gold, score):

        """
        Args:
            gold: The amount of gold the player currently has
            score: The player's current score

        Raises:
            Many questions.

        :type gold: int
        :type score: int
        """

        self.gold = gold
        self.score = score

    def update(self):
        """
        This handles the updating of any attributes of an instance of Player
        """
