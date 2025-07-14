"""
Example utility functions for demonstration purposes.
This module provides basic utility functions that can be tested.
"""


def add_numbers(a, b):
    """Add two numbers together.
    
    Args:
        a (int|float): First number
        b (int|float): Second number
        
    Returns:
        int|float: Sum of a and b
    """
    return a + b


def multiply_numbers(a, b):
    """Multiply two numbers together.
    
    Args:
        a (int|float): First number
        b (int|float): Second number
        
    Returns:
        int|float: Product of a and b
    """
    return a * b


def format_greeting(name):
    """Format a greeting message.
    
    Args:
        name (str): Name to include in greeting
        
    Returns:
        str: Formatted greeting message
    """
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"


class Calculator:
    """Simple calculator class for demonstration."""
    
    def __init__(self):
        """Initialize calculator."""
        self.history = []
    
    def add(self, a, b):
        """Add two numbers and store in history."""
        result = add_numbers(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers and store in history."""
        result = multiply_numbers(a, b)
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()