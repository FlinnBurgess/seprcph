"""
This module contains the all classes relating to the players of the game.

Name:
    player

File:
    seprcph/city.py

Classes:
    Player
"""
class Player():
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
        """

        self.gold = gold
        self.score = score

    def update(self):
        """
        This handles the updating of any attributes of an instance of Player at the change of a turn
        """
        pass
