import unittest
import os

from seprcph import config

class TestConfig(unittest.TestCase):
    path = os.path.join(os.path.expanduser('~'), 'seprcph', 'config')

    def _create_default_config(self):
        s = '[general]\nlogging_level = ERROR\n' \
            'log_file = ~/.config/seprcph/log.txt'
        self._create_config(s)

    def _create_config(self, config_string):
        def _touch_dir(self, path):
            """
            A helper function to create a directory if it doesn't exist.
            path: A string containing a full path to the directory to be created.
            """
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        _touch_dir(path)
        with open(path, 'w') as f:
            f.write(config_string)

class TestDataTypeReplacement(unittest.TestCase):

    def test_replace_true(self):
        self.assertEqual(config.Config._replace_data_types({'': 'true'})[''], True)
        self.assertEqual(config.Config._replace_data_types({'': 'True'})[''], True)
        self.assertEqual(config.Config._replace_data_types({'': 'on'})[''], True)

    def test_replace_false(self):
        self.assertEqual(config.Config._replace_data_types({'': 'false'})[''], False)
        self.assertEqual(config.Config._replace_data_types({'': 'False'})[''], False)
        self.assertEqual(config.Config._replace_data_types({'': 'off'})[''], False)
