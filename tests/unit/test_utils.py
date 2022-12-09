from logless.utils import truncate


class TestUtils:
    """
    Testing suite for util functions
    """
    test_string = "aaaqwertybbbb"

    def test_truncate(self):
        actual_string = truncate(self.test_string, 10)
        assert actual_string == "aaa...bbbb"

    def test_truncate_no_length(self):
        actual_string = truncate(self.test_string, None)
        assert actual_string == self.test_string

