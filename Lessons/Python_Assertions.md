# 1. Python Assertions

Assertions are  statements that you can use to set sanity checks during the development process. Assertions allow you to test the correctness of your code by checking if some specific conditions remain true, which can come in handy while you’re debugging code.

```.pycon
from q33 import mystery
import pytest

def test_mystery():
    assert mystery([1,2,3,4,5],[3,4,5,7,6])==[3,4,5]
    assert mystery([1, 2, 3, 4, 5], [5, 7, 6,2,4]) == [5]
```

Here, the result is:
```pycon
============================= test session starts ==============================
collecting ... collected 1 item

test_q33.py::test_mystery FAILED                                         [100%]
test_q33.py:3 (test_mystery)
[2, 4, 5] != [3, 4, 5]

Expected :[3, 4, 5]
Actual   :[2, 4, 5]
```
**So even if you put 2 asserts in one function, it will only return the last one**