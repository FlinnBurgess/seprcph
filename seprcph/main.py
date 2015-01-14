"""
This module contains the main game loop as well as the system for setting up the file logger.
"""

import logging
import os.path
import platform
import pygame
from seprcph.config import Config
from seprcph.map import Map
from seprcph.track import Track
from seprcph.train import Train
from seprcph.event import Event, EventManager
from seprcph.ui import initialise_ui
from seprcph.goal_factory import GoalFactory
from seprcph.ui_elements import Window, Container, Label
from seprcph.player import Player
from seprcph.deck import Deck
from seprcph.card_factory import CardFactory

active_player = None

def initialise_players(goal_factory, game_map):
    global active_player
    card_factory = CardFactory()
    placeholder_deck = Deck("Placeholder",
                            card_factory.build_cards(50, "aggressive"), None)
    player1 = Player(500, 0, placeholder_deck)
    player2 = Player(500, 0, placeholder_deck)

    player1.goals = goal_factory.build_goals(3, player1, game_map)
    player2.goals = goal_factory.build_goals(3, player2, game_map)
    active_player = player1

    return player1, player2

def initialise_trains(player1, player2, cities):
    img = pygame.image.load(os.path.join(Config.general['image_dir'], 'train.png'))
    train_one = Train(player1, 100, 100, cities.keys()[0], 0, img)
    train_two = Train(player2, 100, 100, cities.keys()[1], 0, img)
    return train_one, train_two

def change_player(event):
    global active_player
    if active_player == player1:
        active_player = player2
    else:
        active_player = player1

def main():
    """
    The game loop and glue code.
    """
    effect_selection = False
    effect = None
    goal_factory = GoalFactory()

    def _set_effect_selection(event):
        effect = event.effect
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        effect_selection = True

    def _unset_effect_selection(event):
        effect = None
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        effect_selection = False

    def _change_turn(event):
        if active_player == player1:
            active_player = player2
        else:
            active_player = player1

        if active_player.goals < 5:
            active_player.goals = goal_factory.build_goals(1, active_player, game_map.cities)

        if active_player.hand.size < 5:
            active_player.hand.draw_cards(2)

        turns += 1

    EventManager.add_listener('card.triggered', _set_effect_selection)
    EventManager.add_listener('effect.applied', _unset_effect_selection)
    EventManager.add_listener('turns.changed', _change_turn)

    if platform.system() == 'Windows':
        Config.load_config(os.path.join(os.path.expanduser('~'), 'seprcph',
                                            'config.cfg'))
    else:
        Config.load_config(os.path.join(os.path.expanduser('~'), '.config',
                                            'seprcph', 'config.cfg'))

    logger = setup_file_logger(Config.logging['file'],
                            (Config.logging['format'],
                            Config.logging['date_format']),
                            Config.logging['level'])
    logging.info(str(Config))

    screen, clock = initialise_pygame()
    FPS = Config.graphics['fps']

    game_map = Map(pygame.image.load(os.path.join(Config.general['image_dir'], 'map.png')))
    player1, player2 = initialise_players(goal_factory, game_map)

    sprites = pygame.sprite.LayeredUpdates()
    sprites.add(game_map._tracks, layer=0)
    sprites.add(game_map._cities.keys(), layer=1)
    sprites.add(initialise_trains(player1, player2, game_map._cities), layer=2)

    EventManager.notify_listeners(Event('window.resize', old_size=game_map.image.get_size(), size=screen.get_size()))
    game_map.image = pygame.transform.scale(game_map.image, screen.get_size())

    sprites.draw(game_map.image)
    screen.blit(game_map.image, (0, 0))
    pygame.display.flip()

    while True:
        # This will block if there isn't an event.
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            return
        elif event.type == pygame.VIDEORESIZE:
            EventManager.notify_listeners(Event('window.resize', size=event.dict['size'], old_size=screen.get_size()))
            for sprite in sprites:
                if isinstance(sprite, Track):
                    sprite._calc_length()
            screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
            screen.blit(pygame.transform.scale(game_map.image, event.dict['size']), (0, 0))
            pygame.display.flip()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return
        elif event.type == pygame.MOUSEBUTTONUP:
            clicked = [s for s in sprites if s.rect.collidepoint(event.pos)]
            if not clicked:
                continue
            if effect_selection:
                # We're trying to find which object the effect should be
                # applied to.
                ev = Event('ui.select_effect', obj=clicked[-1], pos=event.pos)
            else:
                ev = Event('ui.clicked', obj=clicked[-1], pos=event.pos)
            EventManager.notify_listeners(ev)

        clock.tick(FPS)
        sprites.draw(game_map.image)
        pygame.display.flip()

def initialise_pygame():
    """
    Intialise pygame modules, then the screen and finally the clock.

    Returns:
        A two element tuple - with screen first and then clock.
    """
    pygame.init()
    if Config.general['fullscreen']:
        screen = pygame.display.set_mode((Config.general['screen_width'],
                                        Config.general['screen_height']),
                                        pygame.FULLSCREEN | pygame.RESIZABLE)
    else:
        screen = pygame.display.set_mode((Config.general['screen_width'],
                                        Config.general['screen_height']), pygame.RESIZABLE)

    pygame.display.set_caption('Trains across Europe')
    clock = pygame.time.Clock()
    logging.debug("%s", pygame.display.Info())
    return screen, clock

def setup_file_logger(filename, formatting, log_level):
    """
    A helper function for creating a file logger.

    Args:
        filename: The file that shall be logged to.
        formatting: A tuple containing the log format and then the date format.
        log_level: The level of logging to be reported.

    Returns:
        logger: A complete logger object.
    """
    logger = logging.getLogger()
    # If a stream handler has been attached, remove it.
    if logger.handlers:
        logger.removeHandler(logger.handlers[0])
    handler = logging.FileHandler(filename)
    logger.addHandler(handler)
    formatter = logging.Formatter(*formatting)
    handler.setFormatter(formatter)
    logger.setLevel(log_level)
    handler.setLevel(log_level)
    return logger

if __name__ == '__main__':
    main()
