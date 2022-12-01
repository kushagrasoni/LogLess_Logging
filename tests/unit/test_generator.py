import os

from conf.config import MODE_CONFIG, INFO


class TestGenerator:
    """
    Testing suite for the Generator class
    """

    event_type = "test event type"
    assign_type = "test assign type"
    var_name = "test var name"
    var_value = "test var value"
    level = INFO

    def test_get_mode_config_not_set(self, generator):
        """
        Tests getting logging mode configurations without prior setting
        """
        os.environ["LOGGING_MODE"] = ""
        expected_mode_config = MODE_CONFIG.get("SAFE")
        actual_mode_config = generator.get_mode_config()
        assert expected_mode_config == actual_mode_config

    def test_get_mode_config_set(self, generator):
        """
        Tests getting logging mode configurations with predefined setting
        """
        os.environ["LOGGING_MODE"] = "DEV"
        expected_mode_config = MODE_CONFIG.get("DEV")
        actual_mode_config = generator.get_mode_config()
        assert expected_mode_config == actual_mode_config

    def test_log(self, generator, mocker):
        mock_log_info = mocker.patch.object(generator, "log_info")
        generator.log(self.event_type, self.assign_type, self.var_name, self.var_value, self.level)
        mock_log_info.assert_called_once_with(self.event_type, self.assign_type, self.var_name, self.var_value)

    def test_log_unsupported(self, generator, mocker):
        mock_log_info = mocker.patch.object(generator, "log_info")
        generator.log(self.event_type, self.assign_type, self.var_name, self.var_value, "UNSUPPORTED")
        mock_log_info.assert_not_called()

    def test_log_info_with_values(self, generator, mocker):
        mock_logger = mocker.patch.object(generator, "logger")
        generator.log_info(self.event_type, self.assign_type, self.var_name, self.var_value)
        mock_logger.info.assert_called_once_with(f"{self.event_type}, {self.assign_type}, {self.var_name}, "
                                                 f"{self.var_value}")
