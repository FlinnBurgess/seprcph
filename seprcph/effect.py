"""
Holds the class for an effect
"""
from seprcph.event import EventManager


class Effect(object):
    """
    Represents an effect that can be applied ot an object.

    Listens for click events and then applies its effect if the object
    that was clicked is the same type as this effect works with.
    """
    def __init__(self, name, target_type, effect, undo, turns):
        """
        Get everything setup and notify the EventManager that we want to listen
        for events.

        Args:
            name: The name of the effect
            target_type: The class that th target is required to be
            effect: A function of the form: func(target) that will be applied to the target
            undo: A function of the form: func(target) that will be applied to the target once this effect has ended
            turns: The amount of turns this effect is active for
        """
        assert turns >= 1
        self.name = name
        self.target_type = target_type
        self.effect = effect
        self.undo = undo
        self.turns = turns

        EventManager.add_listener('ui.clicked', self.apply)

    def apply(self, event):
        """
        Applies the effect to the target.

        Args:
            event: The event sent to us from the topic 'ui.clicked'.

        Returns:
            True if successful, False otherwise.
        """
        if isinstance(event.obj, self.target_type):
            self.effect(event.obj)
            event.obj.add_effect(self)
            return True
        return False

    def remove(self, target):
        """
        Called when an effect has run out to set the target back to its original state

        Args:
            target: The object that the effect was applied to

        Raises:
            AssertionError
        """
        assert isinstance(target, self.target_type)
        self.undo(target)

class Affectable(object):
    def __init__(self):
        self.effects = []

    def add_effect(self, eff):
        self.effects.append(eff)

    def remove_dead_effects(self):
        dead_eff = [e for e in self.effects if e.turns == 0]
        for eff in dead_eff:
            eff.undo(self)

        self.effects = [e for e in self.effects if not e.turns == 0]

    def decrement_turns(self):
        for eff in self.effects:
            eff.turns -= 1

        self.remove_dead_effects()
