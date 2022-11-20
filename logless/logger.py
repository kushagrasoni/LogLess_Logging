# importing module
import logging

# Create and configure logger
logging.basicConfig(filename="app/app.log",
                    format='%(asctime)s | %(levelname)s | %(message)s\n',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)