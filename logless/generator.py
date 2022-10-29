import logging
import os
import secrets

from conf.config import MODE_CONFIG


class Generator:
    def __init__(self, config, patterns, vars):
        """
        Constructor method
        """
        self.logger = logging.getLogger()
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
            if pattern.get("verbosity") == "INFO":
                self.log_info(pattern)

    def log_info(self, pattern):
        msg = ""
        msg += secrets.choice(self.config.get("STATIC_MSG").get("VERBOSITY").get("INFO"))
        # Extract attributes from pattern

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
