"""
This module contains the main game loop as well as the system for setting up the file logger.

Name:
    main

File:
    seprcph/main.py

Functions:
    main
    setup_file_logger
"""

import logging
import pygame
from pygame.locals import *
from seprcph.config import Config


def main():
    """
    The game loop and glue code.
    """
    Config.load_config()
    logger = setup_file_logger(Config.logging['file'],
                            (Config.logging['format'],
                            Config.logging['date_format']),
                            Config.logging['level'])
    logging.info("Config.general is " + str(Config.general))
    logging.info("Config.logging is " + str(Config.logging))

    screen, clock = initialise_pygame()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

def initialise_pygame():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Trains across Europe')
    clock = pygame.time.Clock()
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
