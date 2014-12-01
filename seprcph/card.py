from event import Event, EventManager


class Card(object):
    """
    Class describing the buff/debuff cards
    """
    def __init__(self, name, id, description, effect, image):
        """
        Args:
            name: The name of the Card
            id: A unique identifier
            description: A description of the effect
            effect: An effect callback
            image: The image file to be displayed with the card in the GUI
        """
        self.name = name
        self.id = id
        self.desc = description
        self.effect = effect
        self.image = image

    def __repr__(self):
        return "<name: %s, ID: %d, description: %s>" \
        % (self.name, self.id, self.desc)

    def trigger(self):
        """
        Activates the card's effect.
        NOT the same as playing a card. This method is in the Hand class.
        """
        EventManager.notify_listeners(Event('card.triggered',
                                        effect=self.effect))
