import pytest

from conf.config import LOG_CONFIG
from logless.generator import Generator

# register plugins
pytest_plugins = []


# initialize fixtures
@pytest.fixture(scope="session")
def generator():
    """
    Fixture for the log generator
    """
    # TODO: Define patterns for this fixture
    patterns = [{}]
    gen = Generator(LOG_CONFIG, patterns, None)
    return gen
