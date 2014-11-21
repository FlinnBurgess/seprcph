import unittest
import errno
import os

from seprcph import config


class TestConfig(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove(os.path.join(os.path.expanduser('~'),
                            'seprcph', 'config'))
        except OSError as err:
            if err.errno != errno.ENOENT:
                raise

    def test_default_config(self):
        config.Config.create_default_config()
        config.Config.load_config()
        self.assertIn('logging_level', config.Config.general)

    def test_empty_config(self):
        config.Config.load_config()
        self.assertIn('logging_level', config.Config.general)

    def test_incomplete_general_heading(self):
        config.Config.create_config('[gener]')
        self.assertRaises(config.IncompleteConfigurationFile, config.Config.load_config)

    def test_missing_general_heading(self):
        config.Config.create_config('[test]')
        self.assertRaises(config.IncompleteConfigurationFile, config.Config.load_config)


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
