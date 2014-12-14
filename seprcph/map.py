""" For big-daddy home-slice
"""

import pygame

from track_matrix import TrackMatrix
from city import City

class Map(object):
    def __init__(self, cities, tracks, image):
        """
	Create the map object from list of cities and a list of tracks

	Args:
		cities: List of city objects
                tracks: List of track objects
                image: A pygame surface
	"""
        self._cities = cities
        self._tracks = tracks
        self._track_matrix = TrackMatrix(cities, tracks)
        self.image = image
