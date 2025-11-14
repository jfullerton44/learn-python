# Exercise 12: Pandas Basics

## Concept
DataFrames/Series, reading files, data manipulation (selecting, filtering, groupby), handling missing data.

## AI/ML Application
Dataset analysis, feature engineering, data cleaning, EDA.

## Your Task
1. `create_dataframe(data_dict)` - Create DataFrame from dict
2. `filter_by_condition(df, column, value)` - Filter rows where column == value
3. `group_and_aggregate(df, group_col, agg_col, func)` - Group by column and aggregate
4. `handle_missing(df, strategy)` - Handle NaN values ('drop' or 'fill')
5. `select_columns(df, columns)` - Select specific columns
6. `add_computed_column(df, col_name, func)` - Add new column from function

## Testing
```bash
pytest exercises/12_pandas_basics/test_pandas_basics.py -v
```
