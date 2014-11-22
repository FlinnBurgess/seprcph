import ConfigParser
import os.path
import errno
import platform


class IncompleteConfigurationFileError(Exception):
    """
    Raised when the general section is missing from a config file.
    """
    pass


class Config(object):
    """
    A static class for loading and storing configuration.
    """
    general = {}

    @staticmethod
    def load_config():
        """
        Read the contents of a predefined configuration file and load it into
        dictionaries.

        If a configuration file doesn't exist at the predefined location, a
        new one is created.

        Raises:
            IncompleteConfigurationFileError
        """
        if platform.system() == 'Windows':
            path = os.path.join(os.path.expanduser('~'), 'seprcph', 'config.cfg')
        else:
            path = os.path.join(os.path.expanduser('~'), '.config', 'seprcph', 'config.cfg')
        conf = ConfigParser.SafeConfigParser()
        # Maintain the case of the config file.
        conf.optionxform = str
        if not os.path.exists(path):
            Config.create_default_config()

        conf.read(path)
        if 'general' not in conf._sections:
            raise IncompleteConfigurationFileError('Missing general section')
        Config.general = Config._replace_data_types(conf._sections['general'])

    @staticmethod
    def _replace_data_types(dictionary):
        """
        Replaces strings with appropriate data types (int, boolean).

        Also replaces the human readable logging levels with the integer form.

        Args:
            dictionary: A dictionary returned from the config file.

        Returns:
            A dictionary with strings converted to data types.
        """

        def _is_numeric(string):
            """
            Python 2 is braindead and doesn't implement .isnumeric() for
            strings, this is a hack to get that functionality.

            Args:
                string: The string that shall be checked.

            Raises:
                ValueError
            """
            try:
                int(string)
                return True
            except ValueError:
                return False

        logging_levels = {
            'NONE': 0, 'NULL': 0, 'DEBUG': 10, 'INFO': 20, 'WARNING': 30,
            'ERROR': 40, 'CRITICAL': 50}
        for key, val in dictionary.items():
            if val in ['true', 'True', 'on']:
                dictionary[key] = True
            elif val in ['false', 'False', 'off']:
                dictionary[key] = False
            elif key == 'log_file' and '~' in val:
                dictionary[key] = val.replace('~', os.path.expanduser('~'))
            elif val in logging_levels:
                dictionary[key] = logging_levels[val]
            elif isinstance(val, str) and _is_numeric(val):
                dictionary[key] = int(val)
            elif ',' in val:
                dictionary[key] = [x.lstrip() for x in val.split(',')]
        return dictionary

    @staticmethod
    def create_default_config():
        """
        Create a basic config that has just enough to allow the game
        to run.
        """
        if platform.system() == 'Windows':
            conf = '[general]\nlogging_level = ERROR\n' \
                'log_file = ~/seprcph/log.txt'
        else:
            conf = '[general]\nlogging_level = ERROR\n' \
                'log_file = ~/.config/seprcph/log.txt'
        Config.create_config(conf)

    @staticmethod
    def create_config(config_string):
        """
        Write a string to the config file.

        Args:
            config_string: The string to be written to the config file

        Raises:
            OSError
        """
        path = os.path.join(os.path.expanduser('~'), 'seprcph', 'config')
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as err:
            if err.errno != errno.EEXIST:
                raise
        with open(path, 'w') as conf_file:
            conf_file.write(config_string)
