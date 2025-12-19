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
