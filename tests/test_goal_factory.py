import unittest
import platform
import os
import errno
import pygame
from seprcph.goal_factory import GoalFactory
from seprcph.config import Config
from seprcph.map import Map
from seprcph.player import Player
from seprcph.deck import Deck
from seprcph.card import Card

if platform.system() == 'Windows':
    path = os.path.join(os.getcwd(), 'config.cfg')
else:
    path = os.path.join(os.getcwd(), 'config.cfg')

def setUpModule():
    Config.load_config(path)
    Config.general['data_dir'] = os.path.join(os.getcwd(), 'data')
    Config.general['image_dir'] = os.path.join(os.getcwd(), 'assets', 'images')

def tearDownModule():
    try:
        os.remove(path)
    except OSError as err:
        if err.errno != errno.ENOENT:
            raise

class TestCreateGoal(unittest.TestCase):

    def setUp(self):
        image = pygame.Surface((10, 10))
        self.goal_factory = GoalFactory()
        self.deck = Deck(None, [Card('card1', None, None, None, image),
                            Card('card2', None, None, None, image)], None)
        self.player = Player(0, 0, self.deck)
        self.map = Map(image)

    def test_create_one_goal(self):
        self.goal_factory.build_goals(1, self.player, self.map)
