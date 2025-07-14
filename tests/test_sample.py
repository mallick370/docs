"""
Sample test file to demonstrate CI/CD workflow functionality.
This can be expanded when actual Python code is added to the project.
"""
import pytest


def test_sample():
    """A simple test to verify pytest is working."""
    assert True


def test_basic_math():
    """Test basic mathematical operations."""
    assert 2 + 2 == 4
    assert 10 - 5 == 5
    assert 3 * 4 == 12


def test_string_operations():
    """Test basic string operations."""
    test_string = "Hello, World!"
    assert "Hello" in test_string
    assert test_string.upper() == "HELLO, WORLD!"
    assert len(test_string) == 13


class TestExampleClass:
    """Example test class to demonstrate test organization."""
    
    def test_list_operations(self):
        """Test list operations."""
        test_list = [1, 2, 3, 4, 5]
        assert len(test_list) == 5
        assert 3 in test_list
        assert test_list[0] == 1
        assert test_list[-1] == 5
    
    def test_dict_operations(self):
        """Test dictionary operations."""
        test_dict = {"key1": "value1", "key2": "value2"}
        assert "key1" in test_dict
        assert test_dict["key1"] == "value1"
        assert len(test_dict) == 2