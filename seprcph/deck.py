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
            graveyard: The player's graveyard

        """

        self.cards = cards
        self.deck = deck
        self.size = len(self.cards)

    def draw(self):
        """
        Places the card at the top of the Deck into the Hand.
        """
        self.cards.append(deck.pop())

    def discard(self, index):
        """
        Removes the card from self.cards[index] and places it in the graveyard.
        """
        self.deck.graveyard.append(self.cards.pop(index))

    def resize(self):
        """
        Checks that the Hand is of the appropriate size.
        If not, discards cards of the player's choosing until the hand has been reduced to the right size.

        """
        if self.size <= 7:
            pass
        else:
            while self.size > 7:
                discard_index = int(raw_input("Enter the index of the card to discard: "))
                self.discard(discard_index)

    def play(self, index):
        """
        Triggers the effect of the Card at the index, then discards it.

        """
        self.cards[index].trigger()
        self.discard(index)

    def update(self):
        """
        Method to be run at the start of the player's turn.
        First checks if the Deck is empty. If so, restarts the Deck.
        Then draws two cards and runs the re-sizer.

        """
        if self.deck.size == 0:
            self.deck.restart()

        self.draw()
        self.resize()
