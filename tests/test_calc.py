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
        """check the difference is as expected, when normal inputs are provided"""
        expected_result = 40
        actual_result = subtract(list_2_integers)
        assert actual_result == expected_result

    def test_subtract_less_than_zero(self):
        """check that if the difference of two numbers is negative, the function coerces it to zero"""
        expected_result = 0
        actual_result = subtract([5, 10])
        assert actual_result == expected_result

    def test_subtract_large_list(self, list_5_integers):
        """check that subtract() handles a list input >2 elements by raising
        expected exception"""
        expected_exception_msg = f"function needs a list of 2. yours has {len(list_5_integers)} elements"
        with pytest.raises(ValueError) as e:
            subtract(list_5_integers)
        assert e.match(expected_exception_msg)
    
    @pytest.mark.skip
    def test_subtract_empty_list(self):
        pass

@pytest.mark.skip
class TestsMultiply:
    """test normal, exceptions, and basic edge cases of multiply()"""

    def test_multiply_normal(self, list_2_integers):
        """check the product is as expected, when normal inputs are provided"""
    
    def test_multiply_empty_list(self):
        pass

@pytest.mark.skip
class TestsDivide:
    """test normal, exceptions, and basic edge cases of divide()"""

    def test_divide_normal(self, list_2_integers):
        """check the product is as expected, when normal inputs are provided"""
        pass

    def test_divide_by_zero(self, list_2_integers):
        """check the product is as expected, when normal inputs are provided"""
        pass

    def test_divide_large_list(self, list_5_integers):
        pass
