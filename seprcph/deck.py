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


class Hand(object):
    """
    Class describing the Hand object
    """

    def __init__(self, cards, deck):
        """
        Args:
            cards: A list containing the cards in the hand
            deck: The Deck instance with which the Hand is associated
        """
        self.cards = cards
        self.deck = deck
        self.size = len(self.cards)

    def draw_cards(self, count):
        """
        Places the cards at the top of the Deck into the Hand.

        Args:
            count: The amount of cards to be drawn
        """
        for _ in xrange(count):
            self.cards.append(self.deck.pop())
        self.size += count

    def discard(self, index):
        """
        Removes the card from self.cards[index] and places it in the graveyard.

        Args:
            index: The index of the card to be removed.
        """
        self.deck.add_to_discard(self.cards.pop(index))
        self.size -= 1

    def play(self, index):
        """
        Triggers the effect of the Card at the index, then discards it.
        Args:
            index: The index of the card to be played
        """
        self.cards[index].trigger()
        self.discard(index)

    def update(self):
        """
        Method to be run at the start of the player's turn.
        Draws two cards.

        TODO: Add the ability for the user to discard extra cards.
        """
        self.draw_cards(2)
