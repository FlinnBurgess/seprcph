"""
This module contains all classes related to the tracks.
"""

import math
import pygame
from seprcph.renderable import Renderable
from seprcph.effect import Affectable


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


class Track(Renderable, Affectable):
    """
    Manages the data to be stored about a Track.

    Also provides functions that allow Players to interact with Tracks.
    """
    def __init__(self, start_city, end_city, gold_generation, cost):
        """
        Args:
            start_city: One of the two cities that will be placed inside the
                        cities set.
            end_city: The second of two cities that will be placed inside the
                      cities set.
            gold_generation: The amount of gold generated per turn by the track
                             for the player.
            cost: The cost of unlocking the track.
        """
        self.cities = (start_city, end_city)
        self.gold_generation = gold_generation
        self.cost = cost
        self.rotation = self._calc_rotation(start_city.pos, end_city.pos)

        super(Track, self).__init__(((start_city.pos[0] + end_city.pos[0]) /2,
                                    (start_city.pos[1] + end_city.pos[1]) / 2))
        Affectable.__init__(self)

        self.is_locked = True
        self.owner = None

    def __repr__(self):
        return "<connects: %s, %s, gold-gen: %d, cost: %d>" \
               % (str(self.cities[0]),
                  str(self.cities[1]),
                  self.gold_generation,
                  self.cost)

    def update(self):
        """
        Tells the game how to maintain tracks on each refresh
        """
        self.owner.gold += self.gold_generation
        self.decrement_turns()

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

    def _calc_rotation(self, first_p, second_p):
        """
        Calculate the counterclockwise rotation (in degrees) required to line
        the track's image up with both cities.

        Args:
            first_p: The position tuple of a city.
            second_p: The position tuple of another city.
        """
        xdiff = first_p[0] - second_p[0]
        ydiff = first_p[1] - second_p[1]
        return math.degrees(math.atan2(xdiff, ydiff))

    def _calc_length(self, first_p, second_p):
        """
        Calculate the length between the two points

        Args:
            first_p: The position tuple of a city.
            second_p: The position tuple of another city.
        """
        xdiff = first_p[0] - second_p[0]
        ydiff = first_p[1] - second_p[1]
        return int(math.sqrt(xdiff ** 2 + ydiff ** 2))

