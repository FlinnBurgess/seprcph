"""
This module contains all classes relating to the city.
"""
from seprcph.renderable import Renderable
from seprcph.effect import Affectable


class City(Renderable, Affectable):
    """
    Class that describes the cities shown on the map
    """
    def __init__(self, name, pos, is_capital, image):
        """
        Args
            name: Name of the city.
            pos: Co-ordinates of the city on the map.
            is_capital: Whether or not the city is the capital of it's
                        respective country.
            image: the image to be used with pygame.surface
        """
        self.name = name
        self.is_capital = is_capital
        super(City, self).__init__(pos, image)
        Affectable.__init__(self)

    def __repr__(self):
        return "<name: %s, coordinates: %s, is_capital: %r>" \
               % (self.name, str(self.pos), self.is_capital)

    def update(self):
        """
        Called each turn.
        """
        pass
