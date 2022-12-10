

class TestProfile:
    """
    Testing suite for the Profile class
    """

    # setup

    def test_wrap_color(self, profile1):
        """
        Tests wrap color value
        """
        text = "test text"
        color = "blue"
        expected_wrap_color_value = f'{profile1.color_map[color]}{text}\u001b[0m'

        actual_wrap_color_value = profile1.wrap_color(text, color)

        assert expected_wrap_color_value == actual_wrap_color_value

    def test_without_colors_and_without_values(self, profile1):
        actual_profile_str = profile1.without_colors(False)
        assert actual_profile_str == f'{profile1.event_type} ==> {profile1.assign_type} "{profile1.var_name}"'

    def test_without_colors_and_with_values(self, profile1):
        actual_profile_str = profile1.without_colors(True)
        assert actual_profile_str == f'{profile1.event_type} ==> {profile1.assign_type} "{profile1.var_name}" with ' \
                                     f'value = "{profile1.var_value}"'

    def test_with_color_and_with_values(self, profile1):
        actual_profile_str = profile1.with_colors(True)
        assert actual_profile_str == f'{profile1.wrap_color(profile1.event_type, "blue")} ==> ' \
                                     f'{profile1.wrap_color(profile1.assign_type, "yellow")} ' \
                                     f'"{profile1.wrap_color(profile1.var_name, "magenta")}" ' \
                                     f'with value = "{profile1.wrap_color(profile1.var_value, "green")}"'
