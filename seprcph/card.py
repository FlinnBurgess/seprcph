"""
This module contains all classes relating to cards.

Name:
    card

File:
    seprcph/card.py

Classes:
    Card
"""
from seprcph.config import Config
from seprcph.event import Event, EventManager
import pygame


class Card(object):
    """
    Class describing the buff/debuff cards
    """
    def __init__(self, name, description, type, effect, image):
        """
        Args:
            name: The name of the Card
            description: A description of the effect
            type: The type of the card
            effect: An effect callback
            image: The image file to be displayed with the card in the GUI
        """
        self.name = name
        self.desc = description
        self.effect = effect
        self.type = type

        # We can't use convert_alpha without a screen being set up, so test
        # if a screen is set up.
        try:
            image = image.convert_alpha()
        except pygame.error:
            pass
        finally:
            self.image = image

    def __repr__(self):
        return "<name: %s, description: %s>" % (self.name, self.desc)

    def trigger(self):
        """
        Activates the card's effect.
        NOT the same as playing a card. This method is in the Hand class.
        """
        EventManager.notify_listeners(Event('card.triggered',
                                            effect=self.effect))
