"""Exercise 19: Datetime"""
from datetime import datetime, timedelta

def parse_date(date_string, format="%Y-%m-%d"):
    return datetime.strptime(date_string, format)

def format_date(dt, format="%Y-%m-%d"):
    return dt.strftime(format)

def add_days(dt, days):
    return dt + timedelta(days=days)

def calculate_duration(start, end):
    return (end - start).total_seconds()

def get_current_timestamp():
    return datetime.now().isoformat()
