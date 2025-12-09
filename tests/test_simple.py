"""
Tests for the package calculator
"""

from calculator.basics import Calculator

def test_add():
    """
    Tests the add method
    """
    c = Calculator()
    assert c.add(1, 2) == 3
