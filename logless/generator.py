from logger import logger
import os
import secrets

from conf.config import MODE_CONFIG, LOG_CONFIG, INFO


class Generator:
    def __init__(self, config, patterns, vars):
        """
        Constructor method
        """
        self.logger = logger
        self.config = config
        self.mode_config = self.get_mode_config()
        self.patterns = patterns
        self.vars = vars

    def log(self):
        """
        Begins logging procedure. It iterates through each pattern and generates an appropriate logging message
        according to the characteristics. The logging messages then gets logged.
        """
        for pattern in self.patterns:
            if pattern.get("verbosity") == INFO and INFO in self.mode_config.get("SUPPORTED_LOG_LEVELS"):
                self.log_info(pattern.get("pattern"))

    def log_info(self, pattern):
        # Extract attributes from pattern
        for spec in pattern:
            if isinstance(spec, tuple):
                msg = ""
                for i in range(len(spec)):
                    # TODO: determine if value should be logged according to configuration {LOG_VALUES}
                    if i == len(spec) - 1:
                        msg += f"{spec[i]}"
                        break
                    msg += f"{spec[i]}, "
                self.logger.info(msg)

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
        print("Mode config selected: ", mode_config)
        return mode_config


if __name__ == "__main__":
    # example usage
    patterns = [{
        "pattern": [('Assign',
                     'Total Targets: 1',
                     'Targets: [<ast.Name object at 0x110d46d60>]',
                     'Value: <ast.Call object at 0x110d46d30>'),
                    ('Name', 'action_event', '<ast.Store object at 0x1104faa90>'),
                    ('Call',
                     '<ast.Attribute object at 0x110d46d00>',
                     1,
                     '[<ast.Constant object at 0x110d46c70>]'),
                    ('Attribute',
                     'Value: <ast.Name object at 0x110d46cd0>',
                     'Attribute: get',
                     'Context: <ast.Load object at 0x1104faa30>'),
                    ('Name', 'event', '<ast.Load object at 0x1104faa30>'),
                    ('Constant', 'action')],
        "verbosity": "INFO"
    }]
    gen = Generator(LOG_CONFIG, patterns, None)
    gen.log()
