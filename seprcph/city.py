__author__ = 'Ethan'
"""
This module contains all classes relating to the city.

NAME
    city

FILE
    seprcph/city.py

CLASSES
    City
"""

class City(object):
    """
    Class that describes the cities shown on the map
    """


    def __init__(self, name, position, is_capital):
        """
        Args
        name: Name of the city.
        position: Co-ordinates of the city on the map.
        is_capital: Whether or not the city is the capital of it's respective country.
        """
        self.name = name
        self.position = ()
        self.is_capital = is_capital

    def update(self):
    pass
    ##I've got literally no idea what should go in here. Sorry.##