import functools
import inspect
import logging
import os
from sys import settrace
from logless.tracer import Tracer
from logless import logger

DISABLED = bool(os.getenv('DISABLE_LOGLESS', ''))


class LogLess:
    """
    This is the decorator which will be used by any function in the application code.
    This decorator is to bused in the following format:

    SYNTAX:
        @log\n
        def function(**args):
            do something\n
            return something

    param mode: The Access mode of the logless decorator with values - SAFE, DEV, PROD
    return: The output of the function (if any)
    """

    def __init__(self, mode=None, file_type=None, file_path='.', file_name='app'):
        self.mode = mode
        self.file_type = file_type
        self.file_path = file_path
        self.file_name = file_name

    def __call__(self, class_or_function):
        print(self.file_name)
        # Update the logger to add file handler in case the file_type = 'txt' or 'pdf' is passed
        if self.file_type == 'txt':
            # logger = logging.getLogger('logless_logger')
            file_handler = logging.FileHandler(f'{self.file_path}/{self.file_name}.log', mode='w')
            logger.addHandler(file_handler)

        if DISABLED:
            return class_or_function

        if inspect.isclass(class_or_function):
            return self._wrap_class(class_or_function)
        else:
            return self._wrap_function(class_or_function)

    def _wrap_class(self, cls):
        for attr_name, attr in cls.__dict__.items():
            if inspect.isfunction(attr):
                setattr(cls, attr_name, self._wrap_function(attr))
        return cls

    def _wrap_function(self, function):
        """
        This is a wrapper method within decorator which takes decorated function as an argument.
        param function: The input is the function to which decorator is used upon
        return: Returns itself
        """
        func_name = function.__name__
        trace = Tracer(func_name, self.mode, self.file_type)

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            """
            This is a wrapper function within the decorator which handles the arguments of the decorated function.
            return: Returns the decorated function call
            """
            settrace(trace.tracer)
            result = function(*args, **kwargs)
            settrace(None)
            return result

        return wrapper
