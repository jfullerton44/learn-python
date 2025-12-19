"""
Exercise 12: Pandas Basics

Complete the implementations below. Run tests to verify your solution.
"""
import pandas as pd
from typing import Dict, List, Callable


def create_dataframe(data_dict: Dict):
    """Create DataFrame from dictionary."""
    # TODO: Implement
    pass



def filter_by_condition(df, column: str, value):
    """Filter rows where column equals value."""
    # TODO: Implement
    pass



def group_and_aggregate(df, group_col: str, agg_col: str, func: str):
    """Group by column and aggregate."""
    # TODO: Implement
    pass



def handle_missing(df, strategy: str='drop'):
    """Handle missing values."""
    # TODO: Implement
    pass



def select_columns(df, columns):
    """Select specific columns."""
    # TODO: Implement
    pass



def add_computed_column(df, col_name: str, func: Callable):
    """Add new column computed from existing data."""
    # TODO: Implement
    pass
