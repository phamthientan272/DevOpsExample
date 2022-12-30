# test_division.py
from division import divide

def test_divide_valid_numbers():
    result = divide(4, 2)
    assert result == {"result": 2}

def test_divide_number_2_zero():
    result = divide(4, 0)
    assert result == {"error": "Cannot divide by zero"}
