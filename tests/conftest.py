import pytest
from unittest.mock import Mock

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
