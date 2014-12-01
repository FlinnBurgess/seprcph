"""
This module contains the all classes relating to the players of the game.

Name:
    player

File:
    seprcph/city.py

Classes:
    Player
"""


class Player(object):
    """
    Player class that represents each player.
    """
    def __init__(self, gold, score, deck, hand):
        """
        Args:
            gold: The amount of gold in the player's bank
            score: The player's current score
            deck: The player's deck
            hand: The cards currently available for the player to use
        """

        self.gold = gold
        self.score = score
        self.deck = deck
        self.hand = hand

    def __repr__(self):
        return "This player has %d gold and %d points" % (self.gold, self.score)

    def update(self):
        """
        This handles the updating of any attributes of an instance of Player at the change of a turn

        """
        pass
