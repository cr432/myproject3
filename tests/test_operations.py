"""
Module containing pytest tests for calculator operations.
This module includes tests for various calculator operations using the Calculation class from the calculator module. 
It ensures that arithmetic operations are performed correctly and that specific edge cases, such as division by zero, are handled appropriately.
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide


def test_operation(a, b, operation, expected):
    '''Testing various operations'''
    calculation = Calculation.create(a, b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
