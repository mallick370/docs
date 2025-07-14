"""
Tests for the utils module.
"""
import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import add_numbers, multiply_numbers, format_greeting, Calculator


class TestUtilityFunctions:
    """Test utility functions."""
    
    def test_add_numbers(self):
        """Test the add_numbers function."""
        assert add_numbers(2, 3) == 5
        assert add_numbers(-1, 1) == 0
        assert add_numbers(0, 0) == 0
        assert add_numbers(10.5, 2.5) == 13.0
    
    def test_multiply_numbers(self):
        """Test the multiply_numbers function."""
        assert multiply_numbers(2, 3) == 6
        assert multiply_numbers(-2, 3) == -6
        assert multiply_numbers(0, 5) == 0
        assert multiply_numbers(2.5, 4) == 10.0
    
    def test_format_greeting(self):
        """Test the format_greeting function."""
        assert format_greeting("Alice") == "Hello, Alice!"
        assert format_greeting("") == "Hello, World!"
        assert format_greeting("Bob") == "Hello, Bob!"


class TestCalculator:
    """Test Calculator class."""
    
    def test_calculator_init(self):
        """Test calculator initialization."""
        calc = Calculator()
        assert calc.history == []
    
    def test_calculator_add(self):
        """Test calculator add method."""
        calc = Calculator()
        result = calc.add(5, 3)
        assert result == 8
        assert "5 + 3 = 8" in calc.get_history()
    
    def test_calculator_multiply(self):
        """Test calculator multiply method."""
        calc = Calculator()
        result = calc.multiply(4, 6)
        assert result == 24
        assert "4 * 6 = 24" in calc.get_history()
    
    def test_calculator_history(self):
        """Test calculator history functionality."""
        calc = Calculator()
        calc.add(1, 2)
        calc.multiply(3, 4)
        
        history = calc.get_history()
        assert len(history) == 2
        assert "1 + 2 = 3" in history
        assert "3 * 4 = 12" in history
    
    def test_calculator_clear_history(self):
        """Test calculator clear history functionality."""
        calc = Calculator()
        calc.add(1, 2)
        calc.multiply(3, 4)
        
        assert len(calc.get_history()) == 2
        calc.clear_history()
        assert len(calc.get_history()) == 0