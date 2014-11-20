#!/usr/bin/python2.7


class Event(object):
    """
    Lightweight class that represents a generic event
    """
    def __init__(self, topic, desc=None, **kwargs):
        self.topic = topic
        self.desc = desc
        self.data = kwargs


class EventManager(object):
    """
    Static class that manages the publishing and handling of messages
    """
    __subscriptions = {}

    @staticmethod
    def add_listener(topic, callback):
        """
        Registers a callback function to respond to events relating to the
        passed topic

        Args:
            topic: The topic to which the listener will subscribe
            callback: The event handler method of the listening object

        Raises:
            SEVERAL QUESTIONS
        """

        EventManager.__subscriptions.setdefault(topic, [])
        EventManager.__subscriptions[topic].append(callback)

    @staticmethod
    def remove_listener(topic, callback):
        """
        De-registers a callback function from the passed topic

        Args:
            topic: The topic form which the listener will be unsubscribed
            callback: The event handler method of the listening object

        Raises:
            SEVERAL QUESTIONS
        """

        EventManager.__subscriptions[topic].remove(callback)

    @staticmethod
    def notify_listeners(event):
        """
        Calls the handling methods of objects listening to the passed topic

        Args:
            event: Object containing the topic and event meta-data

        Raises:
            AssertionError
        """

        assert(event.topic in EventManager.__subscriptions.keys())

        for handler in EventManager.__subscriptions[event.topic]:
            handler(event)
