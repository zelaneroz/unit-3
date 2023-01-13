import q34_oop
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

object1 = q34_oop.quiz34()
def test_valid(object1):
    assert object1.to_roman(num=37)=='XXXVII'