# Invoke at command line with: >> python -m pytest -v tests/test_calc.py

import pytest
from calc import subtract, multiply, divide

@pytest.fixture
def list_2_integers():
    integer1 = 50
    integer2 = 10
    return [integer1, integer2]

@pytest.fixture
def list_5_integers():
    return [1, 2, 3, 4, 5]


class TestsSubtract:
    """test normal, exceptions, and basic edge cases of subtract()"""

    def test_subtract_normal(self, list_2_integers):
        """check the difference is as expected when a list of ints provided"""
        expected_result = 40
        actual_result = subtract(list_2_integers)
        assert actual_result == expected_result

    def test_subtract_less_than_zero(self):
        """check that if the difference of two numbers is negative,
        the function coerces the results to zero
        """
        expected_result = 0
        actual_result = subtract([5, 10])
        assert actual_result == expected_result

    def test_subtract_large_list(self, list_5_integers):
        """check that subtract() raises expected exception when
        a list of more than 2 elements is passed
        """
        expected_exception_msg = f"function needs a list of 2. yours has {len(list_5_integers)} elements"
        with pytest.raises(ValueError) as e:
            subtract(list_5_integers)
        assert e.match(expected_exception_msg)


class TestsMultiply:
    """test normal, exceptions, and basic edge cases of multiply()"""

    def test_multiply_two_ints(self, list_2_integers):
        """check the product is as expected, when list of 2 ints provided"""
        expected_result = 500
        actual_result = multiply(list_2_integers)
        assert actual_result == expected_result

    def test_multiply_many_ints(self, list_5_integers):
        """check the product is as expected with list of more than 2 ints"""
        expected_result = 120
        actual_result = multiply(list_5_integers)
        assert actual_result == expected_result


class TestsDivide:
    """test normal, exceptions, and basic edge cases of divide()"""

    def test_divide_normal(self, list_2_integers):
        """check the quotient is as expected with a list of 2 ints"""
        expected_result = 5.0
        actual_result = divide(list_2_integers)
        assert actual_result == expected_result

    def test_divide_by_zero(self):
        """check the function raises expected exception message
        when a list has a 0 in the denominator position
        """
        list_with_a_zero = [199, 0]
        expected_exception_msg = "cannot divide, the divisor is 0"
        with pytest.raises(ValueError) as e:
            divide(list_with_a_zero)
            e.match(expected_exception_msg)

    def test_divide_large_list(self, list_5_integers):
        """check the function raises expected exception message
        when trying to divide with a list of more than 2 elements
        """
        expected_exception_msg = f"function needs a list of 2. yours has {len(list_5_integers)} elements"
        with pytest.raises(ValueError) as e:
            divide(list_5_integers)
            e.match(expected_exception_msg)