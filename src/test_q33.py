from q33 import mystery
import pytest

def test_mystery():
    assert mystery([1, 2, 3, 4, 5], [5, 7, 6,2,4]) == [2,4,5]