import pytest
from unittest.mock import Mock, patch
import namegetter

@pytest.fixture
def nameGetter():
    return namegetter
