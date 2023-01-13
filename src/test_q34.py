from q34_oop import quiz34
import pytest
#
# def test_valid():
#     assert to_roman(37)=='XXXVII'
#     assert to_roman(44)=='XLIV'
#     assert to_roman(100)=='C'
#
# def test_invalid():
#     with pytest.raises(ValueError):
#         to_roman(101)
def test_valid():
    object1 = quiz34()
    assert object1.to_roman(37)=='XXXVII'