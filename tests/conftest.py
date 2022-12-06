import pytest
from logless.generator import Generator

# register plugins
pytest_plugins = []


# initialize fixture
@pytest.fixture(scope="function")
def generator():
    """
    Fixture for the generator
    """
    gen = Generator()
    return gen
