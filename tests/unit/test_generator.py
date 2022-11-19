import os

from conf.config import MODE_CONFIG


class TestGenerator:
    """
    Testing suite for the Generator class
    """

    def test_get_mode_config_not_set(self, generator):
        """
        Tests getting logging mode configurations without prior setting
        """
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
