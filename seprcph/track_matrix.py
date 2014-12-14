"""
This module contains the classes responsible for managing the connections between cities

Name:
    track_matrix

Location:
    seprcph/track_matrix.py

Classes:
    TrackMatrix
"""
from track import Track
from city import City


class TrackMatrix(object):
    """
    Class that manages the Track objects connecting cities
    """
    def __init__(self, cities, tracks):
        """
            Args:
                cities: List of city objects
                tracks: List of track objects
        """
        # Create a dictionary representation of an enum, mapping a city object
        # to a unique integer
        self._cities = {k: v for v, k in enumerate(cities)}

        # Create an empty n*n matrix where n is the number of cities
        self._matrix = [[None] * len(cities)] * len(cities)

        for track in tracks:
            self.add_track(track)

    def fetch_indices(self, city_pair):
        """
            Args:
                city_pair: A 2-element tuple containing city objects

            Returns:
                A 2 element tuple containing indices for the pair of cities.
        """
        return (self._cities[city_pair[0]],
                self._cities[city_pair[1]])

    def fetch_track(self, city_pair):
        """
            Args:
                city_pair: A 2-element tuple containing city objects

            Returns:
                Either the track object corresponding to the pair of cities
                passed to the method, or None if no such connection exists.
        """
        indices = self.fetch_indices(city_pair)
        return self._matrix[indices[0]][indices[1]]

    def add_track(self, track):
        """
            Args:
                track: The track object to be added.
        """
        i = self.fetch_indices(track.cities_connected)

        self._matrix[i[0]][i[1]] = self._matrix[i[1]][i[0]] = track
