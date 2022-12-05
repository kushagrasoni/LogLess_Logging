import sys

from logless import log
from logless.decorator import my_tracer


class TestDecorator:

    def test_should_call_set_trace(self, mocker):
        """
        Tests the invocation of the tracer
        """
        # have to patch the method wrt location of this project's package (not sys.settrace)
        mock_settrace = mocker.patch('logless.decorator.settrace')

        @log
        def test_function(*args, **kwargs):
            mock_settrace.assert_called_once_with(my_tracer)

        test_function()

    def test_log(self):

        def test_function():
            pass

        actual_function = log(test_function)
        assert callable(actual_function)
