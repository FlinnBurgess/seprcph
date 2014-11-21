__author__ = 'Flinn'
"""
This module contains all classes relating to the trains.

NAME
    train

FILE
    seprcph/train.py

CLASSES
    Train
"""


class Train():
    """
    Train class to represent any trains in existence within the game.
    """

    def __init__(self, buffs, debuffs, speed, capacity):
        """
        Args:
            buffs: A list of buffs that are currently affecting the train
            debuffs: A list of debuffs that are currently affecting the train
            speed: An integer denoting the speed of a train,
                   affecting how far it travels each turn
            capacity: An integer denoting train capacity and
                      therefore how much cargo the train can hold

        Raises:
            The roof

        :type buffs: list
        :type debuffs: list
        :type speed: int
        :type capacity: int
        """
        self.buffs = buffs
        self.debuffs = debuffs
        self.speed = speed
        self.capacity = capacity

    def update(self):
        """
        The update function is used by the game engine to maintain any
        any information about an instance of the train class.

        Raises:
            Who knows what!
        """
        for each_buff in self.buffs:
            if each_buff.timer == 0:
                self.buffs.remove(each_buff)
                # Loops through the buffs checking to see if any
                # have reached the end of their timer, and removes them if so.

        for each_debuff in self.debuffs:
            if each_debuff.timer == 0:
                self.debuffs.remove(each_debuff)
                # Does the same for debuffs

        ## TODO More code will need to be added later

    def apply_effects(self):
        """
        Responsible for applying any buffs or debuffs that the are affecting
        the train at the beginning of the turn.

        Raises:
        """
        for each_buff in self.buffs:
            each_buff.apply()

        for each_debuff in self.debuffs:
            each_debuff.apply()