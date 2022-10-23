import logging
import secrets


class Generator:
    def __init__(self, config, patterns, vars):
        """
        Constructor method
        """
        self.logger = logging.getLogger()
        self.config = config
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
