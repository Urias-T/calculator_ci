"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)
        assert 5 == calculator.add(6, -1)


    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
        assert 5 == calculator.subtract(3, -2)


    def test_multiply(self):
        assert 8 == calculator.multiply(2, 4)


    def test_divide(self):
        assert 6 == calculator.divide(18, 3)
        assert 0.5 == calculator.divide(1, 2)
