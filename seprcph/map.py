""" For big-daddy home-slice
"""

import pygame

from track_matrix import TrackMatrix
from city import City

class Map(object):
    def __init__(self, map_image, cities, tracks):
	""" 
	Create the map object from list of cities and track mappings

	Args:
		cities: List of city objects
		tracks:	Dictionary mapping pairs (2-element tuples) to tuples of track meta-data

	Raises:
		?
	"""

	self._cities = cities
	self._tracks = TrackMatrix(self._cities)

	# Iterate over the passed track dictionary and populate the track matrix
	for k, v in tracks.iteritems():
		self._tracks.add_track(k, v[0], v[1], v[2], v[3])
