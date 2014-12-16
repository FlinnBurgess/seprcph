"""
This module contains all classes relating to the city.

Name:
    city

File:
    seprcph/city.py

Classes:
    City
"""
import pygame


class City(pygame.sprite.Sprite):
    """
    Class that describes the cities shown on the map
    """
    def __init__(self, name, pos, is_capital, image):
        """
        Args
            name: Name of the city.
            pos: Co-ordinates of the city on the map.
            is_capital: Whether or not the city is the capital of it's
                        respective country.
            image: the image to be used with pygame.surface
        """
        super(City, self).__init__()
        self.name = name
        self.pos = pos
        self.is_capital = is_capital

        # We can't use convert_alpha without a screen being set up, so test
        # if a screen is set up.
        try:
            image = image.convert_alpha()
        except pygame.error:
            pass
        finally:
            self.image = image

    def __repr__(self):
        return "<name: %s, coordinates: %s, is_capital: %r>" \
               % (self.name, str(self.pos), self.is_capital)

    @property
    def rect(self):
        """
        Calculate the rect based upon the image size and
        object's position.
        """
        rect = self.image.get_rect()
        rect.centerx = self.pos[0]
        rect.centery = self.pos[1]
        return rect

    def update(self):
        """
        Called each turn.
        """
        pass
