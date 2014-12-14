"""
This is the superclass for all of out UI elements.

Name:
    ui_element

File:
    seprcph/ui_element.py

Classes:
    Element
"""

class Element(object):
    """
    Superclass for the UI elements
    """

    def __init__(self, size, position):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            position: a tuple containing the coordinates of the UI element
        """
        self.size = size
        self.pos = position

    def __repr__(self):
        return "<size: %s, position: %s>" % (self.size, self.pos)

    def draw(self):
        """
        Tells the game how to draw the UI element
        """
        pass
