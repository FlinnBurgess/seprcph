import json
import os.path
import pygame
from config import Config
from city import City
from track import Track


def _objs_from_file(file_path, obj_hook):
    """
    Create a list of objects that are defined within a JSON file.

    The json file needs to contain a list of the objects, with parameters that
    match up to those defined in cls.

    Args:
        file_path: The location of the JSON file to be read.
        obj_hook: A function to convert a dict into a class.
    """
    with open(file_path, 'r') as json_file:
        return json.load(json_file, object_hook=obj_hook)

def create_cities(file_path):

    def _city_hook(kwargs):
        """
        Create a City object from kwargs.

        Args:
            kwargs: A dictionary of elements from the json file.
        """
        kwargs['image'] = pygame.image.load(os.path.join(Config.general['image_dir'], kwargs['image']))
        kwargs['pos'] = tuple(kwargs['pos'])
        return City(**kwargs)

    return _objs_from_file(file_path, _city_hook)

def create_tracks(file_path, cities):
    # Change cities into a dict in the form {city_name: city_obj}
    # so we get the speed of a hashmap when looking up cities by name.
    cities = dict(zip([c.name for c in cities], cities))

    def _track_hook(kwargs):
        """
        Create a Track object from kwargs.

        Args:
            kwargs: A dictionary of elements from the json file.
        """
        kwargs['image'] = pygame.image.load(os.path.join(Config.general['image_dir'], kwargs['image']))
        kwargs['start_city'] = cities[kwargs['start_city']]
        kwargs['end_city'] = cities[kwargs['end_city']]
        return Track(**kwargs)

    tracks = _objs_from_file(file_path, _track_hook)

    return tracks
