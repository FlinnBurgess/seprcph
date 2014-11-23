__author__ = 'Ethan'
"""
This module contains all classes realted to the tracks.

NAME:
    track

LOCATION:
    seprcph/track.py

CLASSES:
    TrackOwnedError
    Track
"""


class TrackOwnedError(Exception):
    """
    Raised when a player tries unlocking a track that is already owned.
    """
    pass


class NotEnoughGoldError(Exception):
    """
    Raised when a player tries unlocking a track without enough gold.
    """
    pass


class Track(object):
    """
    Track class that manages the data held within each track and lets the player interact with the tracks.

    """
    def __init__(self, start_city, end_city, gold_generation, cost):
        """
        Args:
            cities_connected: A set containing the two cities that are connected by
                              the track.
            gold_generation: The amount of gold generated per turn by the track for
                             the player.
            cost: The cost of unlocking the track.
            is_locked: Whether the track is in use by a player.
            owner: The player that owns the track.

        Raises:
            TrackOwnedError
        """

        self.cities_connected = [start_city, end_city]
        self.gold_generation = gold_generation
        self.cost = cost
        self.is_locked = True
        self.owner = None
        self.color = "gray"

    def update(self):
        """
        Tells the game how to maintain tracks on each refresh
        """

        self.owner.gold += self.gold_generation

    def unlock_track(self, player):

        """
        This unlocks a particular stretch of track, recording the new owner and
        updating the player's gold value

        Args:
            player: the player that is unlocking the track
        """
        if (player.gold - self.cost) < 0:
            raise NotEnoughGoldError("You don't have enough gold!")

        if self.is_locked:
            self.is_locked = False
            self.owner = player
            player.gold -= self.cost
            self.color = "black"
        else:
            raise TrackOwnedError('This track is already owned!')