__author__ = 'Flinn'
import pygame

class map(pygame.surface.Surface):
    """
    Class representing the game's map.
    Inherits from the Surface pygame class.
    """

    def __init__(self, adj_matrix):
        """
        Args:
            adj_matrix: An adjeacency matrix
        """
        self.matrix = adj_matrix

    def update(self):
        ##TODO Need to consider things that need updating for the map

    def shortest_route(self, start_city, end_city):
        ##TODO Make an algorithm for finding shortest route, can't properly do this until we know how the matrix is represented

    def connected(self, start_city, end_city):
        ##TODO Decide how we're going to represent the adjacency matrix (numPy, sets etc.)?