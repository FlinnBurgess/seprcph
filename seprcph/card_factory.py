"""
A module for creating Card objects.
"""

import os.path
import random
from seprcph.json_loader import create_cards
from seprcph.config import Config


class CardFactory(object):
    """
    Create a deck of cards.

    Cards are loaded from a JSON file and arranged into a deck based upon a
    bias (often referred to as Policies).
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
