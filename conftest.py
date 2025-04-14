import pytest

from main import *

@pytest.fixture # Add fixture
def collector():
    collector = BooksCollector()
    return collector