import pytest

from logless.generator import Generator

# register plugins
from logless.log_output import LogGenerator

pytest_plugins = []


# initialize fixtures
@pytest.fixture(scope="session")
def generator():
    """
    Fixture for the log generator
    """
    gen = Generator()
    return gen


# initialize fixture
@pytest.fixture(scope="function")
def log_generator():
    """
    Fixture for the log generator
    """
    log_gen = LogGenerator()
    return log_gen
