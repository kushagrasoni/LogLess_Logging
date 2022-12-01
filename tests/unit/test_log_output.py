import os

from conf.config import MODE_CONFIG
from logless.event import Event


class TestLogOutput:
    """
    Testing suite for the LogGenerator class
    """

    # setup
    event1 = Event('line', 'Initializing Variable', 'var', 'ABC', 'INFO')
    event2 = Event('call', 'Starting Variable', 'start', '123', 'INFO')
    event3 = Event('line', 'Updated Variable', 'var', 'XYZ', 'INFO')

    def test_add_event_single(self, log_generator):
        """
        Tests add single event to the log generator
        """
        expected_events_list = [self.event1]

        log_generator.add_event(self.event1)

        assert expected_events_list == log_generator.events

    def test_add_event_method(self, log_generator):
        """
        Tests add multiple events to the log generator
        """
        expected_events_list = [self.event1, self.event2, self.event3]

        log_generator.add_event(self.event1)
        log_generator.add_event(self.event2)
        log_generator.add_event(self.event3)

        assert expected_events_list == log_generator.events

    def test_wrap_color(self, log_generator):
        """
        Tests wrap color value
        """
        text = "test text"
        color = "blue"
        expected_wrap_color_value = f'{log_generator.color_map[color]}{text}\u001b[0m'

        actual_wrap_color_value = log_generator.wrap_color(text, color)

        assert expected_wrap_color_value == actual_wrap_color_value

    def test_print_to_terminal(self, mocker, log_generator):
        """
        Tests that the print function is invoked for print to terminal with a single event
        """
        mock_print = mocker.patch('logless.log_output.print')
        log_generator.add_event(self.event1)

        log_generator.print_to_terminal()

        mock_print.assert_called_once_with(log_generator.with_colors(self.event1))

    def test_print_to_terminal_no_event(self, mocker, log_generator):
        """
        Tests that the print function is not called for print to terminal for no events
        """
        mock_print = mocker.patch('logless.log_output.print')

        log_generator.print_to_terminal()

        mock_print.assert_not_called()

    def test_get_mode_config_not_set(self, log_generator):
        """
        Tests getting logging mode configurations without prior setting
        """
        os.environ["LOGGING_MODE"] = ""
        expected_mode_config = MODE_CONFIG.get("SAFE")
        actual_mode_config = log_generator.get_mode_config()
        assert expected_mode_config == actual_mode_config

    def test_get_mode_config_set(self, log_generator):
        """
        Tests getting logging mode configurations with predefined setting
        """
        os.environ["LOGGING_MODE"] = "DEV"
        expected_mode_config = MODE_CONFIG.get("DEV")
        actual_mode_config = log_generator.get_mode_config()
        assert expected_mode_config == actual_mode_config

    def test_without_colors_and_without_values(self, log_generator):
        log_generator.mode_config = MODE_CONFIG.get("SAFE")
        actual_event_str = log_generator.without_colors(self.event1)
        assert actual_event_str == f"{self.event1.event_type} {self.event1.assign_type} {self.event1.var_name}"

    def test_without_colors_and_with_values(self, log_generator):
        log_generator.mode_config = MODE_CONFIG.get("DEV")
        actual_event_str = log_generator.without_colors(self.event1)
        assert actual_event_str == f"{self.event1.event_type} {self.event1.assign_type} {self.event1.var_name} with " \
                                   f"value = {self.event1.var_value}"
