""" For big-daddy home-slice
"""
import os.path
from config import Config
from json_loader import create_cities, create_tracks
from track_matrix import TrackMatrix


class Map(object):
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
        self._track_matrix = TrackMatrix(self._cities, self._tracks)
        self.image = image
