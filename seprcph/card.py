"""
This module contains all classes relating to cards, as well as the factory
for creating cards

Name:
    card

File:
    seprcph/card.py

Classes:
    Card
    CardFactory
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

class CardFactory(object):
    """
    Load cards from a json file and create the cards that will be entered
    into a deck.
    """

    class UnknownBiasError(Exception):
        """
        Raised when a bias isn't known.
        """
        pass

    BIASES = {'aggressive': [0.25, 0.35, 0.20, 0.20],
            'defensive': [0.35, 0.25, 0.2, 0.2]}

    def __init__(self):
        """
        Load cards from JSON and them sort them by their type.
        """
        cards = create_cards(os.path.join(Config.general['data_dir'], 'cards.json'))
        self.buffs = [x for x in cards if x.type is 'Buff']
        self.debuffs = [x for x in cards if x.type is 'Debuff']
        self.traps = [x for x in cards if x.type is 'Traps']
        self.events = [x for x in cards if x.type is 'Events']

    def build_cards(self, count, bias):
        """
        Create count number of cards.

        Args:
            count: The amount of cards to create.
            bias: The ratio of each kind of card to use.
        """
        if bias not in self.BIASES:
            raise self.UnknownBiasError("Bias %s is unknown" % bias)

        cards = []
        # Buffs
        for _ in int(self.BIASES[bias][0] * count):
            cards.append(random.choice(self.buffs))
        # Debuffs
        for _ in int(self.BIASES[bias][1] * count):
            cards.append(random.choice(self.debuffs))
        # Traps
        for _ in int(self.BIASES[bias][2] * count):
            cards.append(random.choice(self.traps))
        # Events
        for _ in int(self.BIASES[bias][3] * count):
            cards.append(random.choice(self.events))

        if len(cards) < count:
            for _ in xrange(count - len(cards)):
                cards.append(random.choice(self.buffs + self.debuffs
                                            + self.traps + self.events))

        return cards
