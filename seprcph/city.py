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
import pygame


class City(pygame.sprite.Sprite):
    """
    Class that describes the cities shown on the map
    """

    def __init__(self, name, position, is_capital, rect, image):
        """
        Args
            name: Name of the city.
            position: Co-ordinates of the city on the map.
            is_capital: Whether or not the city is the capital of it's
                        respective country.
            rect: the rect to be used with pygame.surface
            image: the image to be used with pygame.surface
        """
        self.name = name
        self.position = position
        self.is_capital = is_capital
        self.rect = rect
        self.image = image

    def update(self):
        pass