# importing module
import logging

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s: %(levelname)s - %(message)s\n')

# Create and configure Console Logger
console_logger = logging.getLogger('logless_console_log')

# create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# add formatter to console handler
console_handler.setFormatter(formatter)
# add console handler to logger
console_logger.addHandler(console_handler)

# Turn off Hierarchy Propagation
console_logger.propagate = False

# Create and configure File Logger
file_logger = logging.getLogger('logless_file_log')



