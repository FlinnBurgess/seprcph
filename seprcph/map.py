""" For big-daddy home-slice
"""
import os.path
from seprcph.config import Config
from seprcph.json_loader import create_cities, create_tracks


class Map(object):
    """
    Represents the tracks and cities of the map.

    Also stores the map's texture.
    """
    def __init__(self, image):
        """
        Create a Map object by loading cities and tracks from json.

        Args:
            image: A pygame surface
        """
        self._cities = create_cities(os.path.join(Config.general['data_dir'],
                                            "cities.json"))
        self._tracks = create_tracks(os.path.join(Config.general['data_dir'],
                                            "tracks.json"), self._cities)

        # Create a dictionary representation of an enum, mapping a city object
        # to a unique integer
        self._cities = {k: v for v, k in enumerate(self._cities)}

        # Create an empty n*n matrix where n is the number of cities
        self._matrix = [[None] * len(self._cities)] * len(self._cities)

        for track in self._tracks:
            self.add_track(track)

        self.image = image

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
        i = self.fetch_indices(track.cities)

        self._matrix[i[0]][i[1]] = self._matrix[i[1]][i[0]] = track
