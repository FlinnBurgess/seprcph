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
