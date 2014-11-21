import ConfigParser
import os.path
import sys


class Config(object):

    general = {}

    @staticmethod
    def load_config():
        path = os.path.join(os.path.expanduser('~'), 'seprcph', 'config')
        conf = configparser.SafeConfigParser()
        # Maintain the case of the config file.
        conf.optionxform = str
        conf.read(path)
        Config.general = Config._replace_data_types(conf.items('general'))

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
            """
            try:
                int(string)
                return True
            except ValueError:
                return False

        logging_levels = {
            'NONE': 0, 'NULL': 0, 'DEBUG': 10, 'INFO': 20, 'WARNING': 30,
            'ERROR': 40, 'CRITICAL': 50}
        for k, v in dictionary.items():
            if v in ['true', 'True', 'on']:
                dictionary[k] = True
            elif v in ['false', 'False', 'off']:
                dictionary[k] = False
            elif k == 'log_file' and '~' in v:
                dictionary[k] = v.replace('~', os.path.expanduser('~'))
            elif v in logging_levels:
                dictionary[k] = logging_levels[v]
            elif isinstance(v, str) and _is_numeric(v):
                dictionary[k] = int(v)
            elif ',' in v:
                dictionary[k] = [x.lstrip() for x in v.split(',')]
        return dictionary
