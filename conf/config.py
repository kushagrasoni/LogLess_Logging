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