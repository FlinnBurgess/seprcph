"""
This module contains the all classes relating to the players of the game.
"""
from seprcph.hand import Hand
from seprcph.event import EventManager

class Player(object):
    """
    Player class that represents each player.
    """
    player_id = 1
    def __init__(self, gold, score, deck, goals=None):
        """
        Args:
            gold: The amount of gold in the player's bank
            score: The player's current score
            deck: The player's deck
            goals: A list containing the player's current goals
        """
        assert deck is not None

        self.gold = gold
        self.score = score
        self.deck = deck
        self.id = Player.player_id
        self.goals = goals
        self.hand = Hand([], self.deck, self.id)

        Player.player_id += 1

        EventManager.add_listener('goal.completed', self.remove_goal)
        EventManager.add_listener('goal.failed', self.remove_goal)


    def __repr__(self):
        return "<Player gold: %d, player points: %d>" % (self.gold, self.score)

    def update(self):
        """
        This handles the updating of any attributes of an instance of Player at the change of a turn

        """
        pass

    def remove_goal(event):
        if event.goal in self.goals:
            self.goals.remove(event.goal)
