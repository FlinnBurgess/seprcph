import unittest

from seprcph import event


class TestCreateEvent(unittest.TestCase):
    
    def test_no_data_event(self):
        e = event.Event('topic', desc='desc')
        self.assertIsNone(e.data)

    def test_correct_event(self):
        e = event.Event('topic', 'desc', one=1)
        self.assertIsNotNone(e)

if __name__ == '__main__':
    unittest.main()
