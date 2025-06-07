# app.operations refers to /app/operations/__init__.py
from app.operations import addition, subtraction, multiplication, division
import pytest

# need to be named with test_ if they are a test
def test_addition():
    assert addition(1,1) == 2

def test_subtraction():
    assert subtraction(1,1) == 0

def test_multiplication():
    assert multiplication(1,1) == 1

# when this succeeds
def test_division_positive():
    assert division(1,1) == 1

# # when this fails
# def test_division_negative():
#     # we are expecting to get this ZeroDivisionError
#     # if you do division(1,1): Failed: DID NOT RAISE <class 'ZeroDivisionError'>
#     with pytest.raises(ZeroDivisionError):
#         division(1,0)

def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)