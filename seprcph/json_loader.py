import json
import os.path
import pygame
from seprcph.config import Config
from seprcph.city import City
from seprcph.track import Track
from seprcph.card import Card


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
    """
    Creates a list of City objects from a JSON file to be used within the game.

    Args:
        file_path: The location of the JSON file to be read.
    """

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
    """
    Creates a list of Track objects to be used within the game.

    Args:
        file_path: The location of the JSON file to be read.
        cities: A dictionary containing cities to be used as start/end cities.
    """
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

    return  _objs_from_file(file_path, _track_hook)

def create_cards(file_path):
    """
    Create a list of cards.

    Args:
        filepath: The location of the JSON file.
    """
    def _card_hook(kwargs):
        """
        Create a Card object from kwargs.

        Args:
            kwargs: A dictionary of elements from the json file.
        """
        kwargs['image'] = pygame.image.load(os.path.join(Config.general['image_dir'], kwargs['image']))
        return Card(**kwargs)

    return _objs_from_file(file_path, _card_hook)
