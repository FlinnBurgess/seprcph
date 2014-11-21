import unittest
import os

from seprcph import config

PATH = os.path.join(os.path.expanduser('~'), 'seprcph', 'config')

class TestConfig(unittest.TestCase):

    def test_default_config(self):
        config.Config._create_default_config()
        config.Config.load_config()
        self.assertIn('logging_level', config.Config.general)

class TestDataTypeReplacement(unittest.TestCase):

    def test_replace_true(self):
        self.assertEqual(config.Config._replace_data_types({'': 'true'})[''], True)
        self.assertEqual(config.Config._replace_data_types({'': 'True'})[''], True)
        self.assertEqual(config.Config._replace_data_types({'': 'on'})[''], True)

    def test_replace_false(self):
        self.assertEqual(config.Config._replace_data_types({'': 'false'})[''], False)
        self.assertEqual(config.Config._replace_data_types({'': 'False'})[''], False)
        self.assertEqual(config.Config._replace_data_types({'': 'off'})[''], False)

    def test_expand_user(self):
        self.assertEqual(config.Config._replace_data_types({'log_file': '~'})['log_file'], os.path.expanduser('~'))

    def test_replace_int(self):
        self.assertEqual(config.Config._replace_data_types({'': '1'})[''], 1)

    def test_replace_list(self):
        self.assertEqual(config.Config._replace_data_types({'': '1, 2, 3'})[''], ['1', '2', '3'])

    def test_replace_log_level(self):
        for level, value in {'NONE': 0, 'NULL': 0, 'DEBUG': 10, 'INFO': 20,
                        'WARNING': 30, 'ERROR': 40, 'CRITICAL': 50}.items():
            self.assertEqual(config.Config._replace_data_types({'': level})[''], value)

if __name__ == '__main__':
    unittest.main()
