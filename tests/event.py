import unittest

from seprcph import event

x = 0

def _func(_):
    x = 1

class TestCreateEvent(unittest.TestCase):

    def test_no_data_event(self):
        e = event.Event('topic', 'desc')
        self.assertEqual(e.data, {})

    def test_no_desc_event(self):
        e = event.Event('topic', foo=2)
        self.assertIsNone(e.desc)

    def test_correct_event(self):
        e = event.Event('topic', 'desc', foo=2)
        self.assertIsNotNone(e)

class TestEventManager(unittest.TestCase):

    def test_attach_listener(self):
        event.EventManager.add_listener('foo', _func)
        self.assertEqual(len(event.EventManager._subscriptions), 1)

    def test_notify_unknown_listener(self):
        self.assertRaises(AssertionError, event.EventManager.notify_listeners, event.Event('bar'))

    def test_notify_listeners(self):
        event.EventManager.notify_listeners(event.Event('foo'))
        self.assertEqual(x, 1)

    def test_remove_listener(self):
        event.EventManager.remove_listener('foo', _func)
        self.assertEqual(len(event.EventManager._subscriptions['foo']), 0)

if __name__ == '__main__':
    unittest.main()
