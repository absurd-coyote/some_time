import pytest
import sys

from unittest.mock import Mock, MagicMock

@pytest.fixture
def store():
    return MagicMock()

@pytest.fixture
def time_counter():
    return Mock()

@pytest.fixture
def input_trigger():
    return Mock()

@pytest.fixture
def input_memory():
    return Mock()

@pytest.fixture
def output_display():
    return Mock()

@pytest.fixture
def output_memory():
    return Mock()


def display(*args, **kwargs):
    breakpoint()
    pass

module = type(sys)('pyscript')
module.display = Mock()  # display
sys.modules['pyscript'] = module
