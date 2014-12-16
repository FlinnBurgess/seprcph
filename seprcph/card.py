"""
This module contains all classes relating to cards.

Name:
    card

File:
    seprcph/card.py

Classes:
    Card
"""
import os.path
import random
from seprcph.config import Config
from seprcph.event import Event, EventManager
from seprcph.json_loader import create_cards



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

class CardFactory(object):

    class UnknownBiasError(Exception):
        """
        Raised when a bias isn't known.
        """
        pass

    BIASES = {'aggressive': [10, 15, 15, 10],
            'defensive': [15, 10, 10, 15]}

    def __init__(self):
        cards = create_cards(os.path.join(Config.general['data_dir'], 'cards.json'))
        self.buffs = [x for x in cards if x.type is 'Buff']
        self.debuffs = [x for x in cards if x.type is 'Debuff']
        self.traps = [x for x in cards if x.type is 'Traps']
        self.events = [x for x in cards if x.type is 'Events']

    def create_cards(self, count, bias):
        if bias not in self.BIASES:
            raise self.UnknownBiasError("Bias %s is unknown" % bias)

        cards = []
        # Buffs
        for _ in self.BIASES[bias][0]:
            cards.append(random.choice(self.buffs))
        # Debuffs
        for _ in self.BIASES[bias][1]:
            cards.append(random.choice(self.debuffs))
        # Traps
        for _ in self.BIASES[bias][2]:
            cards.append(random.choice(self.traps))
        # Events
        for _ in self.BIASES[bias][3]:
            cards.append(random.choice(self.events))

        return cards
