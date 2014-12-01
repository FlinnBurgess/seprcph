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
        self.cards = cards
        self.image = image
        self.graveyard = []
        self.size = len(self.cards)

    def __repr__(self):
        return "<Deck-name: %s, deck-size: %s, graveyard-size: %s>" \
        % (self.character, self.size, len(self.graveyard))

    def shuffle(self):
        """
        Shuffles the deck. Uses Sattolo's algorithm.

        """
        i = len(self.cards)
        while i > 1:
            i = i - 1
            j = random.randrange(i)  # 0 <= j <= i-1
            self.cards[j], self.cards[i] = self.cards[i], self.cards[j]

    def pop(self):
        """
        Returns the card at the top of the deck.

        """
        self.cards.pop(0)

    def restart(self):
        """
        Moves all the cards in the Graveyard back into the Deck and shuffles.

        """
        self.cards.append(self.graveyard)
        self.graveyard = []
        self.shuffle()



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
