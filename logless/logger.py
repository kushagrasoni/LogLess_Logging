# importing module
import logging

# Create and configure logger
# formatter = logging.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s\n')
logger = logging.getLogger('logless_logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
