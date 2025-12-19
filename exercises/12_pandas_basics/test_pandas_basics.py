"""
Tests for Exercise 12: Pandas Basics
"""
import pytest
import pandas as pd
import numpy as np
from exercise import (
    create_dataframe, filter_by_condition, group_and_aggregate,
    handle_missing, select_columns, add_computed_column
)


def test_create_dataframe():
    df = create_dataframe({'A': [1, 2], 'B': [3, 4]})
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['A', 'B']


def test_filter_by_condition():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'x']})
    result = filter_by_condition(df, 'B', 'x')
    assert len(result) == 2
    assert list(result['A']) == [1, 3]


def test_group_and_aggregate():
    df = pd.DataFrame({'group': ['A', 'A', 'B'], 'value': [1, 2, 3]})
    result = group_and_aggregate(df, 'group', 'value', 'sum')
    assert len(result) == 2


def test_handle_missing_drop():
    df = pd.DataFrame({'A': [1, np.nan, 3]})
    result = handle_missing(df, 'drop')
    assert len(result) == 2


def test_handle_missing_fill():
    df = pd.DataFrame({'A': [1, np.nan, 3]})
    result = handle_missing(df, 'fill')
    assert result['A'].iloc[1] == 0


def test_select_columns():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
    result = select_columns(df, ['A', 'C'])
    assert list(result.columns) == ['A', 'C']


def test_add_computed_column():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    result = add_computed_column(df, 'C', lambda row: row['A'] + row['B'])
    assert 'C' in result.columns
    assert list(result['C']) == [4, 6]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
