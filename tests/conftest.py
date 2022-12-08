import pytest

from conf.config import INFO, ERROR
from logless.generator import Generator
from logless.profile import Profile

# register plugins
pytest_plugins = []


# initialize fixtures
@pytest.fixture(scope="function")
def generator():
    """
    Fixture for the generator
    """
    gen = Generator()
    return gen


@pytest.fixture(scope="session")
def profile1():
    """
    Fixture for profile 1
    """
    return Profile('line', 'Initializing Variable', 'var', 'ABC', INFO)


@pytest.fixture(scope="session")
def profile2():
    """
    Fixture for profile 2
    """
    return Profile('call', 'Starting Variable', 'start', '123', "UNSUPPORTED")


@pytest.fixture(scope="session")
def profile3():
    """
    Fixture for profile 3
    """
    return Profile('line', 'Updated Variable', 'var', 'XYZ', ERROR)
