"""Tests for Exercise 18"""
import pytest
from exercise import find_emails, extract_numbers, validate_phone, replace_dates

def test_find_emails():
    text = "Contact: user@example.com or admin@test.org"
    emails = find_emails(text)
    assert len(emails) == 2

def test_extract_numbers():
    assert extract_numbers("I have 2 apples and 5 oranges") == [2, 5]

def test_validate_phone():
    assert validate_phone("123-456-7890") == True
    assert validate_phone("1234567890") == False

def test_replace_dates():
    assert replace_dates("Date: 12/31/2024") == "Date: 2024-12-31"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
