import pytest

from logless.generator import Generator

# register plugins
pytest_plugins = []


# initialize fixtures
@pytest.fixture(scope="session")
def generator():
    """
    Fixture for the log generator
    """
    gen = Generator()
    return gen
