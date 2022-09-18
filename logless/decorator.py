import inspect
from logless.logger import logger
from logless.patterns import get_patterns
from logless.create import get_log


def log(func):
    """
    This is the decorator which will be used by any function in the application code.
    This decorator is to bused in the following format:

    SYNTAX:
        @log\n
        def function(**args):
            do something\n
            return something
    :param func: The input is the function to which decorator is used upon
    :return: The output of the function (if any)
    """
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
