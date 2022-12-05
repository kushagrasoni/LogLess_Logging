import sys

import logless
from logless.logless import Tracer


class TestDecorator:

    def test_should_call_set_trace(self, mocker):
        """
        Tests the invocation of the tracer
        """
        # have to patch the method wrt location of this project's package (not sys.settrace)
        mock_settrace = mocker.patch('logless.decorator.settrace')

        @logless.log()
        def test_function(*args, **kwargs):
            mock_settrace.assert_called_once_with(Tracer().tracer)

        test_function()
