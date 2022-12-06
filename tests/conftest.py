import pytest

from logless.generator import Generator

# register plugins
from logless.generator import LogGenerator

pytest_plugins = []


# initialize fixtures
@pytest.fixture(scope="session")
def generator():
    """
    Fixture for the log generator
    """
    gen = Generator()
    return gen


# initialize fixtur
@pytest.fixture(scope="function")
def log_generator():
    """
    Fixture for the log generator
    """
    log_gen = LogGenerator()
    return log_gen
