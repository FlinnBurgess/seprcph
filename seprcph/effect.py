"""
Holds the class for an effect
"""
from seprcph.event import EventManager, Event


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

        EventManager.add_listener('ui.select_effect', self.apply)

    def apply(self, event):
        """
        Applies the effect to the target.

        Args:
            event: The event sent to us from the topic 'ui.clicked'.
        """
        if isinstance(event.obj, self.target_type):
            self.effect(event.obj)
            event.obj.add_effect(self)
            EventManager.notify_listeners(Event('effect.applied', obj=event.obj))

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
    """
    A mixin style class that can be used to add support for effects.
    """
    def __init__(self):
        """
        Initialise the effects to nothing
        """
        self.effects = []

    def add_effect(self, eff):
        """
        Add an effect to the object's internal list.

        This is called by the eff after it has applied itself to the object.

        Args:
            eff: The effect to be applied
        """
        self.effects.append(eff)

    def _remove_dead_effects(self):
        """
        Called automatically after a turn change. Cleans up effects that are no
        longer active.
        """
        dead_eff = [e for e in self.effects if e.turns == 0]
        for eff in dead_eff:
            eff.undo(self)

        self.effects = [e for e in self.effects if not e.turns == 0]

    def decrement_turns(self):
        """
        Called each turn in order to reduce the number of turns each effect has
        left. Effects with 0 turns left are removed.
        """
        for eff in self.effects:
            eff.turns -= 1

        self._remove_dead_effects()
