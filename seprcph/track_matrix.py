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

    def __init__(self, city_list):
        """
            Args:
                city_list: List of strings representing the cities between which tracks can be built

            Raises:
        """

        # Create a dictionary representation of an enum, mapping the string representation of a city to a unique integer
        self._cities = dict(map(lambda e: (e[1].lower(), e[0]), enumerate(city_list)))

        # Create an empty n*n matrix where n is the number of cities
        self._matrix = [[]]
        self._matrix = [[None for c in city_list] for i in xrange(0, len(city_list))]

    def fetch_indices(self, city_pair):
        """
            Args:
                city_pair: A 2-element tuple containing city objects

            Returns:
                A 2-element tuple containing integers corresponding to the pair of cities passed as arguments
        """
        return (self._cities[city_pair[0].name.lower()],
                self._cities[city_pair[1].name.lower()])

    def fetch_track(self, city_pair):
        """
            Args:
                city_pair: A 2-element tuple containing city objects

            Returns:
                Either the track object corresponding to the pair of cities passed to the method, or None if no such connection exists
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
