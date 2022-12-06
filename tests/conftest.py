import pytest
from logless.generator import LogGenerator

# register plugins
pytest_plugins = []


# initialize fixture
@pytest.fixture(scope="function")
def log_generator():
    """
    Fixture for the log generator
    """
    log_gen = LogGenerator()
    return log_gen
