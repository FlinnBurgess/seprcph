#!/usr/bin/python2.7
"""
This module contains all classes relating to events and their publishing

Name:
    event

File:
    seprcph/event.py

Classes:
    Event
    EventManager
"""


class CallbackAlreadyRegistered(Exception):
    pass


class Event(object):
    """
    Lightweight class that represents a generic event
    """
    def __init__(self, topic, desc=None, **kwargs):
        """
        Constructor for Event class

        Args:
            topic: String denoting the topic that the event relates to
            desc: String, optional, for displaying the event textually
            **kwargs: Optional data arguments for event handlers to use
        """
        self.topic = topic
        self.desc = desc
        self.data = kwargs

    def __repr__(self):
        return "%s | %s : %s" % (self.topic, self.desc, self.data)


class EventManager(object):
    """
    Static class that manages the publishing and handling of messages
    """
    _subscriptions = {}

    @staticmethod
    def add_listener(topic, callback):
        """
        Registers a callback function to respond to events relating to the
        passed topic
        Args:
            topic: The topic to which the listener will subscribe
            callback: The event handler method of the listening object
        Raises:
            CallbackAlreadyRegistered
        """
        EventManager._subscriptions.setdefault(topic, [])
        if callback in EventManager._subscriptions[topic]:
            raise CallbackAlreadyRegistered('Callback %s has already been '
                            'registered to topic: %s' % (callback, topic))
        EventManager._subscriptions[topic].append(callback)

    @staticmethod
    def remove_listener(topic, callback):
        """
        De-registers a callback function from the passed topic

        Args:
            topic: The topic form which the listener will be unsubscribed
            callback: The event handler method of the listening object
        """
        EventManager._subscriptions[topic].remove(callback)
        if len(EventManager._subscriptions[topic]) == 0:
            del EventManager._subscriptions[topic]

    @staticmethod
    def notify_listeners(event):
        """
        Calls the handling methods of objects listening to the passed topic

        Args:
            event: Object containing the topic and event meta-data

        Raises:
            AssertionError
        """
        assert event.topic in EventManager._subscriptions.keys()

        for handler in EventManager._subscriptions[event.topic]:
            handler(event)
