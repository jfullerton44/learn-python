# Exercise 19: Working with Dates and Times

## Concept

The datetime module provides classes for manipulating dates and times, essential for tracking experiments, logging, and scheduling.

### Key Concepts

1. **datetime objects**: Represent dates and times
2. **strptime/strftime**: Parse and format date strings
3. **timedelta**: Represent differences between dates/times
4. **ISO format**: Standard date/time string format

## AI/ML Application

- Logging training run timestamps
- Scheduling model retraining
- Time-series data processing

## Code Examples

### Creating `datetime` Objects

```python
from datetime import datetime, date, time

# Create a specific date and time
dt = datetime(2024, 3, 15, 14, 30, 0)
print(dt)  # 2024-03-15 14:30:00

# Get the current date and time
now = datetime.now()
today = date.today()
print(now)    # e.g., 2024-06-01 10:15:30.123456
print(today)  # e.g., 2024-06-01
```

### Parsing Strings with `strptime`

```python
from datetime import datetime

date_str = "2024-03-15"
dt = datetime.strptime(date_str, "%Y-%m-%d")
print(dt)  # 2024-03-15 00:00:00

timestamp = "15/03/2024 14:30"
dt2 = datetime.strptime(timestamp, "%d/%m/%Y %H:%M")
print(dt2)  # 2024-03-15 14:30:00
```

### Formatting with `strftime`

```python
from datetime import datetime

dt = datetime(2024, 3, 15, 14, 30)
print(dt.strftime("%Y-%m-%d"))         # 2024-03-15
print(dt.strftime("%B %d, %Y"))        # March 15, 2024
print(dt.strftime("%I:%M %p"))         # 02:30 PM
```

### `timedelta` — Calculate Durations

```python
from datetime import datetime, timedelta

start = datetime(2024, 1, 1)
end = datetime(2024, 3, 15)

duration = end - start
print(duration.days)             # 74
print(duration.total_seconds())  # 6393600.0

# Add or subtract time
future = start + timedelta(days=30, hours=12)
print(future)  # 2024-01-31 12:00:00
```

### ISO Format

```python
from datetime import datetime

dt = datetime(2024, 3, 15, 14, 30, 0)
iso_str = dt.isoformat()
print(iso_str)  # 2024-03-15T14:30:00

# Parse an ISO format string back to datetime
parsed = datetime.fromisoformat("2024-03-15T14:30:00")
print(parsed)  # 2024-03-15 14:30:00
```

## Your Task

1. `parse_date(date_string, format="%Y-%m-%d")` - Parse string to datetime
2. `format_date(dt, format="%Y-%m-%d")` - Format datetime to string
3. `add_days(dt, days)` - Add days to a datetime using timedelta
4. `calculate_duration(start, end)` - Return duration in seconds between datetimes
5. `get_current_timestamp()` - Return current time in ISO format

## Testing
```bash
pytest exercises/19_datetime/test_datetime.py -v
```
