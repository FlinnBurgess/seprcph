import unittest

from seprcph.event import Event, EventManager, CallbackAlreadyRegistered


x = 0

def _func(_):
    global x
    x = 1

class TestCreateEvent(unittest.TestCase):

    def test_no_desc_event(self):
        e = Event('topic', foo=2)
        self.assertIsNone(e.desc)

    def test_correct_event(self):
        e = Event('topic', 'desc', foo=2)
        self.assertIsNotNone(e)


class TestEventManager(unittest.TestCase):

    def tearDown(self):
        EventManager._subscriptions = {}

    def setUp(self):
        EventManager.add_listener('foo', _func)

    def test_notify_unknown_listener(self):
        self.assertRaises(AssertionError, EventManager.notify_listeners,
                        Event('bar'))

    def test_attach_already_registered_callback(self):
        self.assertRaises(CallbackAlreadyRegistered,
        EventManager.add_listener, 'foo', _func)

    def test_notify_listeners(self):
        EventManager.notify_listeners(Event('foo'))
        self.assertEqual(x, 1)

    def test_remove_listener(self):
        before = len(EventManager._subscriptions)
        EventManager.remove_listener('foo', _func)
        self.assertEqual(len(EventManager._subscriptions), before - 1)
