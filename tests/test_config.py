import unittest
import ConfigParser
import errno
import os
import platform

from seprcph.config import Config, IncompleteConfigurationFileError

if platform.system() == 'Windows':
    path = os.path.join(os.getcwd(), 'config.cfg')
else:
    path = os.path.join(os.getcwd(), 'config.cfg')


class TestConfig(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove(path)
        except OSError as err:
            if err.errno != errno.ENOENT:
                raise

    def test_default_config(self):
        conf = ConfigParser.RawConfigParser()
        Config.create_default_config(path, conf)
        Config.load_config(path)
        self.assertIn('level', Config.logging)

    def test_empty_config(self):
        Config.load_config(path)
        self.assertIn('level', Config.logging)

class TestDataTypeReplacement(unittest.TestCase):

    def test_replace_true(self):
        self.assertEqual(Config._replace_data_types({'': 'true'})[''], True)
        self.assertEqual(Config._replace_data_types({'': 'True'})[''], True)
        self.assertEqual(Config._replace_data_types({'': 'on'})[''], True)

    def test_replace_false(self):
        self.assertEqual(Config._replace_data_types({'': 'false'})[''], False)
        self.assertEqual(Config._replace_data_types({'': 'False'})[''], False)
        self.assertEqual(Config._replace_data_types({'': 'off'})[''], False)

    def test_expand_user(self):
        self.assertEqual(Config._replace_data_types({'file': '~'})['file'], os.path.expanduser('~'))

    def test_replace_int(self):
        self.assertEqual(Config._replace_data_types({'': '1'})[''], 1)

    def test_replace_list(self):
        self.assertEqual(Config._replace_data_types({'': '1, 2, 3'})[''], ['1', '2', '3'])

    def test_replace_log_level(self):
        for level, value in {'NONE': 0, 'NULL': 0, 'DEBUG': 10, 'INFO': 20,
                        'WARNING': 30, 'ERROR': 40, 'CRITICAL': 50}.items():
            self.assertEqual(Config._replace_data_types({'': level})[''], value)

if __name__ == '__main__':
    unittest.main()
