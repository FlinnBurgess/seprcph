"""
This module contains the all classes relating to the players of the game.
"""
from seprcph.hand import Hand

class Player(object):
    """
    Player class that represents each player.
    """
    def __init__(self, gold, score, deck):
        """
        Args:
            gold: The amount of gold in the player's bank
            score: The player's current score
            deck: The player's deck
        """
        assert deck is not None

        self.gold = gold
        self.score = score
        self.deck = deck
        self.hand = Hand([], self.deck)

    def __repr__(self):
        return "<Player gold: %d, player points: %d>" % (self.gold, self.score)

    def update(self):
        """
        This handles the updating of any attributes of an instance of Player at the change of a turn

        """
        pass
