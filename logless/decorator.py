import inspect
from logless.logger import logger
# import logging
from logless.patterns import get_patterns
from logless.create import get_log

# # Configure Logger
# logger = logging.getLogger()
# formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
#
# file_handler = logging.FileHandler('app.log')
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)
#
# logger.addHandler(file_handler)
# logger.debug('This is a log message!')


# logging.warning('This will get logged to a file')

def log(func):
    def getcode(*args, **kwargs):
        func(*args, **kwargs)
        source_code = inspect.getsource(func)
        for line in source_code.split('\n'):
            line = line.strip()  # needs alog for determining the indentation for various logics

            # Filtering out the unwanted lines like Comments and decorators of Function declarations
            if line and (line[0] not in ['#', '@']) and not line.startswith('def'):
                pattern = get_patterns(line)
                log_statement = get_log(pattern)
                logger.info(log_statement)
                # print(line)
        print('App Output:')
        return func(*args, **kwargs)

    return getcode
