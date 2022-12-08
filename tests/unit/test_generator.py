import os

from conf.config import MODE_CONFIG
from logless.profile import Profile


class TestGenerator:
    """
    Testing suite for the Generator class
    """

    # setup

    def test_add_profile_single(self, generator, profile1):
        """
        Tests add single profile to the generator
        """
        expected_profiles_list = [profile1]

        generator.add_profile(profile1)

        assert expected_profiles_list == generator.profiles

    def test_add_profile_multiple(self, generator, profile1, profile2, profile3):
        """
        Tests add multiple profiles to the generator
        """
        expected_profiles_list = [profile1, profile2, profile3]

        generator.add_profile(profile1)
        generator.add_profile(profile2)
        generator.add_profile(profile3)

        assert expected_profiles_list == generator.profiles

    def test_print_to_terminal(self, mocker, generator, profile1):
        """
        Tests that the print function is invoked for print to terminal with a single profile
        """
        mock_print = mocker.patch('logless.generator.print')
        generator.add_profile(profile1)

        generator.print_to_terminal()

        mock_print.assert_called_once_with(profile1.with_colors(generator.mode_config.get("LOG_VALUES")))

    def test_print_to_terminal_no_profile(self, mocker, generator):
        """
        Tests that the print function is not called for print to terminal for no profiles
        """
        mock_print = mocker.patch('logless.generator.print')

        generator.print_to_terminal()

        mock_print.assert_not_called()

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
        generator.mode = "DEV"
        expected_mode_config = MODE_CONFIG.get("DEV")
        actual_mode_config = generator.get_mode_config()
        assert expected_mode_config == actual_mode_config

    def test_print_to_txt(self, generator, profile1):
        filename = 'test_file.txt'
        try:
            generator.add_profile(profile1)
            generator.print_to_txt(filename)
            with open(filename, 'r') as f:
                line = f.readline()
                assert line != ""
            f.close()
        finally:
            os.remove(filename)

    def test_log(self, mocker, generator, profile1):
        mock_logger = mocker.patch.object(generator, "logger")
        generator.add_profile(profile1)
        generator.log()
        mock_logger.info.assert_called_once_with(profile1.with_colors(generator.mode_config.get("LOG_VALUES")))

    def test_log_unsupported(self, mocker, generator, profile2):
        mock_logger = mocker.patch.object(generator, "logger")
        generator.add_profile(profile2)
        generator.log()
        mock_logger.assert_not_called()

    def test_log_error(self, mocker, generator, profile3):
        mock_logger = mocker.patch.object(generator, "logger")
        generator.add_profile(profile3)
        generator.log()
        mock_logger.error.assert_called_once_with(profile3.without_colors(generator.mode_config.get("LOG_VALUES")))

    def test_allow_event_by_frequency_exists_and_prod(self, generator):
        generator.mode_config = MODE_CONFIG.get("PROD")
        assert generator.allow_event_by_frequency("line")

    def test_allow_event_by_frequency_exists_and_dev(self, generator):
        generator.mode_config = MODE_CONFIG.get("DEV")
        assert generator.allow_event_by_frequency("call")

    def test_allow_event_by_frequency_not_exists(self, generator):
        generator.mode_config = {"FREQUENCY": None}
        assert not generator.allow_event_by_frequency("return")
