import logging

from seprcph import config

def main():
    config.Config.load_config()
    setup_file_logger(config.Config.logging['file'],
                                (config.Config.logging['format'],
                                config.Config.logging['date_format']),
                                config.Config.logging['level'])
    logging.debug("Loaded config file")

def setup_file_logger(filename, formatting, log_level):
    """
    A helper function for creating a file logger.
    Accepts arguments, as it is used in Status and LoggingWriter.
    """
    logger = logging.getLogger()
    # If a stream handler has been attached, remove it.
    if logger.handlers:
        logger.removeHandler(logger.handlers[0])
    handler = logging.FileHandler(filename)
    logger.addHandler(handler)
    formatter = logging.Formatter(formatting)
    handler.setFormatter(formatter)
    logger.setLevel(log_level)
    handler.setLevel(log_level)

if __name__ == '__main__':
    main()
