"""Tests for Exercise 19"""
import pytest
from datetime import datetime
from solution import parse_date, format_date, add_days, calculate_duration, get_current_timestamp

def test_parse_date():
    dt = parse_date("2024-01-15")
    assert dt.year == 2024
    assert dt.month == 1

def test_format_date():
    dt = datetime(2024, 1, 15)
    assert format_date(dt) == "2024-01-15"

def test_add_days():
    dt = datetime(2024, 1, 1)
    new_dt = add_days(dt, 10)
    assert new_dt.day == 11

def test_calculate_duration():
    start = datetime(2024, 1, 1, 10, 0)
    end = datetime(2024, 1, 1, 12, 0)
    assert calculate_duration(start, end) == 7200

def test_get_current_timestamp():
    ts = get_current_timestamp()
    assert isinstance(ts, str)
    assert 'T' in ts

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
