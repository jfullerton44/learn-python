"""Exercise 18: Regex"""
import re

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def extract_numbers(text):
    return [int(x) for x in re.findall(r'\d+', text)]

def validate_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

def replace_dates(text):
    """Replace MM/DD/YYYY with YYYY-MM-DD"""
    return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2', text)
