"""
This module contains all classes relating to cards.
"""
from seprcph.renderable import Renderable
from seprcph.event import EventManager, Event


class Card(Renderable):
    """
    Class describing the buff/debuff cards
    """
    def __init__(self, name, description, type, effect, pos, image):
        """
        Args:
            name: The name of the Card
            description: A description of the effect
            type: The type of the card
            effect: An effect callback
            pos: The position of the card
            image: The image file to be displayed with the card in the GUI
        """
        super(Card, self).__init__(pos, image)
        self.name = name
        self.desc = description
        self.effect = effect
        self.type = type

    def __repr__(self):
        return "<name: %s, description: %s>" % (self.name, self.desc)

    def trigger(self):
        """
        Activates the card's effect.
        NOT the same as playing a card. This method is in the Hand class.
        """
        EventManager.notify_listeners(Event('card.triggered',
                                            effect=self.effect))
