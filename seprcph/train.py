__author__ = 'Flinn'

class Train():
    """
    Train class to represent any trains in existence within the game.
    """

    def __init__(self, buffs, debuffs, speed, capacity):
        """
        Args:
            buffs: A list of buffs that are currently affecting the train
            debuffs: A list of debuffs that are currently affecting the train
            speed: An integer denoting the speed of a train, affecting how far it travels each turn
            capacity: An integer denoting train capacity and therefore how much cargo the train can hold

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
