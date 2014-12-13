import unittest
import json
import errno
import os

from seprcph.json_loader import _objs_from_file

PATH = 'test.json'

class Foo(object):
    def __init__(self, string, integer):
        self.string = string
        self.integer = integer

def obj_hook(kwargs):
    return Foo(**kwargs)

class TestJsonFiles(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove(PATH)
        except OSError as err:
            if err.errno != errno.ENOENT:
                raise

    def test_no_file(self):
        self.assertRaises(IOError, _objs_from_file, '', obj_hook)

    def test_invalid_file(self):
        self.assertRaises(IOError, _objs_from_file, '/foo/', obj_hook)

    def test_empty_file(self):
        with open(PATH, 'w') as f:
            pass
        self.assertRaises(ValueError, _objs_from_file,
                            PATH, obj_hook)

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
        self.assertIsInstance(_objs_from_file(PATH, obj_hook)[0], Foo)

    def test_load_object_int(self):
        self.assertIsInstance(_objs_from_file(PATH, obj_hook)[0].integer, int)

    def test_load_object_str(self):
        self.assertIsInstance(_objs_from_file(PATH, obj_hook)[0].string, unicode)

    def test_load_multpile_objs(self):
        json.dump([{'string': 'test', 'integer': 1},
                        {'string': 'test2', 'integer': 2}], open(PATH, 'w'))
        self.assertEquals(len(_objs_from_file(PATH, obj_hook)), 2)

