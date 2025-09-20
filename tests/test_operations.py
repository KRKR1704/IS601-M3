"""parameterized tests for the operations class"""
import pytest
from app.operations import Operations

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (4.8, 3.3, 8.1),
    (0, 0, 0)
])
def test_addition(a, b, expected):
    result = Operations.addition(a, b)
    assert result == pytest.approx(expected)

@pytest.mark.parametrize("a,b,expected", [
    (3, 2, 1),
    (-4, -5, 1),
    (8.4, 3.3, 5.1),
    (0, 0, 0)
])
def test_subtraction(a, b, expected):
    assert Operations.subtraction(a,b) == pytest.approx(expected)

@pytest.mark.parametrize("a,b,expected", [
    (3, 4, 12),
    (-5, -2, 10),
    (3.0, 3.3, 9.9),
    (0, 0, 0)
])
def test_multiplication(a, b, expected):
    assert Operations.multiplication(a,b) == pytest.approx(expected)

@pytest.mark.parametrize("a,b,expected", [
    (9, 3, 3),
    (-6, 2, -3),
    (6.0, 1.5, 4.0)
])
def test_division(a, b, expected):
    assert Operations.division(a,b) == pytest.approx(expected)

def test_division_by_zero():
    """
    Test that dividing by zero raises a ValueError with the correct message.
    """
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Operations.division(4, 0)