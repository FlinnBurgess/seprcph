import random

class Deck(object):
    """
    Class describing the Decks of cards
    """

    def __init__(self, character, cards, image):
        """
        Args:
            character: The name of the deck
            cards: A list containing all the cards in the deck
            image: The image file to be shown on the Deck selection menu
        """
        self.character = character
        self.discard = []
        self.cards = cards
        self.image = image
        self.size = len(self.cards)

    def __repr__(self):
        return "<deck_name: %s, deck_size: %d" % (self.character, self.size)

    def pop(self):
        """
        Returns the card at the top of the deck.
        """
        if self.size == 0:
            self.restart()
        self.size -= 1
        return self.cards.pop()

    def add_to_discard(self, card):
        """
        Add the card to the discard pile.

        Args:
            card: The card to be added to the discard pile.
        """
        self.discard.append(card)

    def restart(self):
        """
        Moves all the dicarded cards back into the Deck and shuffles.
        """
        self.cards = self.discard
        self.size = len(self.cards)
        random.shuffle(self.cards)
        self.discard = []
