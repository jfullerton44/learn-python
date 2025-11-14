"""
Exercise 12: Pandas Basics
"""
import pandas as pd
from typing import Dict, List, Callable


def create_dataframe(data_dict: Dict) -> pd.DataFrame:
    """Create DataFrame from dictionary."""
    return pd.DataFrame(data_dict)


def filter_by_condition(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    """Filter rows where column equals value."""
    return df[df[column] == value]


def group_and_aggregate(df: pd.DataFrame, group_col: str, agg_col: str, func: str) -> pd.DataFrame:
    """Group by column and aggregate."""
    return df.groupby(group_col)[agg_col].agg(func).reset_index()


def handle_missing(df: pd.DataFrame, strategy: str = 'drop') -> pd.DataFrame:
    """Handle missing values."""
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill':
        return df.fillna(0)
    return df


def select_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Select specific columns."""
    return df[columns]


def add_computed_column(df: pd.DataFrame, col_name: str, func: Callable) -> pd.DataFrame:
    """Add new column computed from existing data."""
    df = df.copy()
    df[col_name] = df.apply(func, axis=1)
    return df


if __name__ == "__main__":
    df = create_dataframe({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print(df)
