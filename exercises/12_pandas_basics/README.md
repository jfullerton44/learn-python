# Exercise 12: Pandas Basics

## Concept
DataFrames/Series, reading files, data manipulation (selecting, filtering, groupby), handling missing data.

## AI/ML Application
Dataset analysis, feature engineering, data cleaning, EDA.

## Code Examples

### DataFrame Creation
```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol"],
    "score": [90, 85, 92],
    "passed": [True, True, True],
})
print(df)
#     name  score  passed
# 0  Alice     90    True
# 1    Bob     85    True
# 2  Carol     92    True
```

### Series
```python
scores = pd.Series([90, 85, 92], name="score")
print(scores.mean())  # 89.0
print(scores.max())   # 92
```

### Filtering Rows
```python
# Boolean indexing
high_scores = df[df["score"] >= 90]
#     name  score  passed
# 0  Alice     90    True
# 2  Carol     92    True

# Filter by exact value
just_bob = df[df["name"] == "Bob"]
```

### groupby — Aggregate by Category
```python
df = pd.DataFrame({
    "dept": ["ML", "ML", "Web", "Web"],
    "name": ["Alice", "Bob", "Carol", "Dave"],
    "salary": [120, 110, 100, 105],
})
avg_salary = df.groupby("dept")["salary"].mean()
# dept
# ML     115.0
# Web    102.5
```

### Handling Missing Data
```python
import numpy as np

df = pd.DataFrame({"a": [1, np.nan, 3], "b": [4, 5, np.nan]})

# Drop rows with any NaN
cleaned = df.dropna()

# Fill NaN with a value (e.g., column mean)
filled = df.fillna(df.mean())
```

### Computed Columns
```python
df = pd.DataFrame({"price": [10, 20, 30], "qty": [2, 1, 3]})
df["total"] = df["price"] * df["qty"]
#    price  qty  total
# 0     10    2     20
# 1     20    1     20
# 2     30    3     90
```

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
