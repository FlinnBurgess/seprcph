"""
This module contains all classes relating to the trains.

Name:
    train

Files:
    seprcph/train.py

Classes:
    Train
"""
import pygame


class Train(pygame.sprite.Sprite):
    """
    Class representing train objects in the game
    """

    def __init__(self, buffs, debuffs, speed, capacity):
        """
        Args:
            buffs: list of buffs currently affecting the train
            debuffs: list of debuffs currently affecting the train
            speed: the speed of the train
            capacity: the capacity of the train
        """
        super(Train, self).__init__()
        self.buffs = buffs
        self.debuffs = debuffs
        self.speed = speed
        self.capacity = capacity

    def update(self):
        pass

    ## TODO apply_effects NEEDS REWORKING - this is a placeholder and does not
    ## TODO fit with the way the cards and decks currently work.
    def apply_effects(self):
        for effect in buffs:
            effect.apply()
        for effect in debuffs:
            effect.apply()