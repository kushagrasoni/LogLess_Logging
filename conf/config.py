# Log levels stored as strings
INFO = "INFO"
DEBUG = "DEBUG"
WARNING = "WARNING"
ERROR = "ERROR"
CRITICAL = "CRITICAL"

LOG_CONFIG = {
    "STATIC_MSG": {
        "VERBOSITY": {
            # Identified top ranked words for different levels from the following paper:
            # Identifying Logging Practices in Open Source Python Containerized Application Projects
            "DEBUG": ["Updated", "Resulted", "Set"],
            "INFO": ["Creating", "Sending", "Deleting", "Stopping"],
            "WARNING": ["Deprecated", "Removed"],
            "ERROR": ["Missing"],
            "CRITICAL": ["Unexpected"]
        }
    }
}

MODE_CONFIG = {
    "SAFE": {
        # this mode does not support all log levels
        "SUPPORTED_LOG_LEVELS": [INFO, DEBUG, ERROR],
        # critical values will not be logged for this mode
        "LOG_VALUES": False,
        # a higher frequency value indicates more logging statements compared to a lower frequency value
        "FREQUENCY": 2
    },
    "DEV": {
        # this mode supports all log levels
        "SUPPORTED_LOG_LEVELS": [INFO, DEBUG, WARNING, ERROR, CRITICAL],
        # critical values will be logged for this mode
        "LOG_VALUES": True,
        # a higher frequency value indicates more logging statements compared to a lower frequency value
        "FREQUENCY": 3
    },
    "PROD": {
        # this mode supports all log levels
        "SUPPORTED_LOG_LEVELS": [INFO, DEBUG, WARNING, ERROR, CRITICAL],
        # critical values will not be logged for this mode
        "LOG_VALUES": False,
        # a higher frequency value indicates more logging statements compared to a lower frequency value
        "FREQUENCY": 1
    }
}
