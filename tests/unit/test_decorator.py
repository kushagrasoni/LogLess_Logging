import sys
from unittest.mock import Mock

import logless


class TestDecorator:

    def test_should_call_set_trace(self, mocker):
        """
        Tests the invocation of the tracer
        """
        # have to patch the method wrt location of this project's package (not sys.settrace)
        mock_settrace = mocker.patch('logless.logless.settrace')
        mock_tracer = mocker.patch('logless.logless.Tracer')
        mock_tracer.return_value.tracer = Mock()

        @logless.log()
        def test_function(*args, **kwargs):
            mock_settrace.assert_called_once_with(mock_tracer.return_value.tracer)

        test_function()

    def test_log(self):

        def test_function():
            pass

        actual_function = logless.log(test_function)
        assert callable(actual_function)
