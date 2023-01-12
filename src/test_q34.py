from q34 import to_roman
import pytest

def test_valid():
    assert to_roman(37)=='XXXVII'
    assert to_roman(44)=='XLIV'
    assert to_roman(100)=='C'

def test_invalid():
    with pytest.raises(ValueError):
        to_roman(101)
