class Player(object):
    """
    Player class that represents each player.
    """

    def __init__(self, gold, score, deck, hand):
        """
        Args:
            gold: The amount of gold in the player's bank
            score: The player's current score
            deck: The player's deck
            hand: The cards currently available for the player to use

        """

        self.gold = gold
        self.score = score
        self.deck = deck
        self.hand = hand

    def update(self):
        """
        This handles the updating of any attributes of an instance of Player at the change of a turn

        """

        self.hand.add(self.deck.pop)
        self.hand.add(self.deck.pop)

        while self.hand.size > 7:
            self.hand.discard()
