import pytest
from aioresponses import aioresponses

@pytest.fixture
def m():
    with aioresponses() as mock:
        yield mock