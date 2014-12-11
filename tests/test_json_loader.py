import unittest
import json
import errno
import os

from seprcph.json_loader import objs_from_json_file

PATH = 'test.json'

class Foo(object):
    def __init__(self, string, integer):
        self.string = string
        self.integer = integer

class TestJsonFiles(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove(PATH)
        except OSError as err:
            if err.errno != errno.ENOENT:
                raise

    def test_no_file(self):
        self.assertRaises(IOError, objs_from_json_file, '', Foo)

    def test_invalid_file(self):
        self.assertRaises(IOError, objs_from_json_file, '/foo/', Foo)

    def test_empty_file(self):
        with open(PATH, 'w') as f:
            pass
        self.assertRaises(ValueError, objs_from_json_file,
                            PATH, Foo)

class TestJsonContents(unittest.TestCase):

    def setUp(self):
        json.dump([{'string': 'test', 'integer': 1}], open(PATH, 'w'))

    def tearDown(self):
        try:
            os.remove(PATH)
        except OSError as err:
            if err.errno != errno.ENOENT:
                raise

    def test_load_object(self):
        self.assertIsInstance(objs_from_json_file(PATH, Foo)[0], Foo)

    def test_load_object_int(self):
        self.assertIsInstance(objs_from_json_file(PATH, Foo)[0].integer, int)

    def test_load_object_str(self):
        self.assertIsInstance(objs_from_json_file(PATH, Foo)[0].string, unicode)

    def test_load_multpile_objs(self):
        json.dump([{'string': 'test', 'integer': 1},
                        {'string': 'test2', 'integer': 2}], open(PATH, 'w'))
        self.assertEquals(len(objs_from_json_file(PATH, Foo)), 2)

