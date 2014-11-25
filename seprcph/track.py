"""
This module contains all classes realted to the tracks.

Name:
    track

Location:
    seprcph/track.py

Classes:
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
            start_city: One of the two cities that will be placed inside the
                        cities_connected set.
            end_city: The second of two cities that will be placed inside the
                      cities_connected set.
            gold_generation: The amount of gold generated per turn by the track for
                             the player.
            cost: The cost of unlocking the track.
        """

        self.cities_connected = [start_city, end_city]
        self.gold_generation = gold_generation
        self.cost = cost
        self.is_locked = True
        self.owner = None

    def __repr__(self):
        return "This track connects %s and %s, costs % gold and generates" \
               "%s gold per turn" % (self.cities_connected[0],
                                     self.cities_connected[1],
                                     self.cost,
                                     self.gold_generation)

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

        Raises:
            TrackOwnedError
            NotEnoughGoldError
        """
        if (player.gold - self.cost) < 0:
            raise NotEnoughGoldError("You don't have enough gold!")

        if self.is_locked:
            self.is_locked = False
            self.owner = player
            player.gold -= self.cost
        else:
            raise TrackOwnedError('This track is already owned!')
        
