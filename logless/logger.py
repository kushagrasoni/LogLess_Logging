# importing module
import logging

# Create and configure logger
logging.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s\n')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
