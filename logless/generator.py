from logless.logger import logger
import os

from conf.config import MODE_CONFIG, INFO


class LogEvent:
    def __init__(self):
        self.event_type = None
        self.event_text = None
        self.type_color_map = {
            'line': 'white',
            'call': 'blue'
        }
        self.color_map = {'black': "\u001b[30m",
                          'red': "\u001b[31m",
                          'green': "\u001b[32m",
                          'yellow': "\u001b[33m",
                          'blue': "\u001b[34m",
                          'magenta': "\u001b[35m",
                          'cyan': "\u001b[36m",
                          'white': "\u001b[37m",
                          'none': ''
                          }

    def generate(self, event_type, event_text):
        self.event_type = event_type
        self.event_text = event_text

    def color_code(self):
        return self.color_map[self.type_color_map[self.event_type]]

    def __str__(self):
        return f'{self.color_code()}{self.event_text}'


class SetColor():
    def __init__(self, text, color='none'):
        self.text = text
        self.color = color
        self.color_map = {'black': "\u001b[30m",
                          'red': "\u001b[31m",
                          'green': "\u001b[32m",
                          'yellow': "\u001b[33m",
                          'blue': "\u001b[34m",
                          'magenta': "\u001b[35m",
                          'cyan': "\u001b[36m",
                          'white': "\u001b[37m",
                          'none': ''
                          }

    def color_code(self):
        return self.color_map[self.color]

    def __str__(self):
        return f'{self.color_code()}{self.text}'


class Generator:
    def __init__(self):
        """
        Constructor method
        """
        self.logger = logger
        self.mode_config = self.get_mode_config()

    def log(self, event, assign_type, var_name, var_value, level):
        """
        Branches into the respective log level method based on the verbosity
        """
        if level == INFO and INFO in self.mode_config.get("SUPPORTED_LOG_LEVELS"):
            self.log_info(event, assign_type, var_name, var_value)

    def log_info(self, event, assign_type, var_name, var_value):
        logging_statement = f'{event}, {assign_type}, {var_name}'
        if self.mode_config.get("LOG_VALUES"):
            logging_statement += f', {var_value}'
        self.logger.info(logging_statement)

    def log_error(self, pattern):
        # TODO
        msg = ""
        self.logger.error(msg)

    # Add remaining verbosity methods

    """ STATIC METHODS """

    @staticmethod
    def get_mode_config():
        """
        Utility function to get environment mode configurations based on environment setting
        """
        # extract environment mode configurations
        mode_config = MODE_CONFIG.get(os.getenv("LOGGING_MODE"))
        if not mode_config:
            # if env var not set correctly, set safe mode as the default
            mode_config = MODE_CONFIG.get("SAFE")
        # print("Mode config selected: ", mode_config)
        return mode_config
