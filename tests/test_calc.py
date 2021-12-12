# Invoke at command line with: >> python -m pytest -v tests/test_calc.py

import pytest
from calc import subtract, multiply, divide

@pytest.fixture
def normal_inputs():
    integer1 = 50
    integer2 = 10
    return [integer1, integer2]

@pytest.fixture
def bad_inputs_list_size_5():
    """some functions, like subtract(), divide() need lists of exactly
    2 elements. this fixture will help test those functions for handling
    > 2 elements.
    """
    return [1, 2, 3, 4, 5]


class TestsSubtract:
    """test normal, exceptions, and basic edge cases of subtract()"""

    def test_subtract_normal(self, normal_inputs):
        """check the difference is as expected, when normal inputs are provided"""
        expected_result = 40
        actual_result = subtract(normal_inputs)
        assert actual_result == expected_result

    def test_subtract_less_than_zero(self):
        """check that if the difference of two numbers is negative, the function coerces it to zero"""
        expected_result = 0
        actual_result = subtract([5, 10])
        assert actual_result == expected_result

    def test_subtract_large_list(self, bad_inputs_list_size_5):
        """check that subtract() handles a list input >2 elements by raising
        expected exception"""
        expected_exception_msg = f"function needs a list of 2. yours has {len(bad_inputs_list_size_5)} elements"
        with pytest.raises(ValueError) as e:
            subtract(bad_inputs_list_size_5)
        assert e.match(expected_exception_msg)
    
    @pytest.mark.skip
    def test_subtract_empty_list(self):
        """do nothing yet"""


@pytest.mark.skip
class TestsMultiply:
    """test normal, exceptions, and basic edge cases of multiply()"""


@pytest.mark.skip
class TestsDivide:
    """test normal, exceptions, and basic edge cases of divide()"""

