# Exercise 18: Regular Expressions Basics

## Concept

Regular expressions (regex) are patterns for matching and manipulating text. Python's `re` module provides powerful pattern matching capabilities.

### Key Concepts

1. **re.findall()**: Find all matches in a string
2. **re.match()**: Match at the beginning of a string
3. **re.sub()**: Replace matches with a pattern
4. **Groups**: Capture parts of matches with parentheses

## AI/ML Application

- Text preprocessing for NLP
- Log parsing and analysis
- Data validation and cleaning

## Code Examples

### `re.findall()` — Find All Matches

```python
import re

text = "Call 555-1234 or 555-5678 for info"
phones = re.findall(r"\d{3}-\d{4}", text)
print(phones)  # ['555-1234', '555-5678']
```

### `re.match()` — Match at the Start of a String

```python
import re

# match() only checks the beginning of the string
result = re.match(r"\d+", "42 is the answer")
print(result.group())  # "42"

result = re.match(r"\d+", "The answer is 42")
print(result)  # None — no match at the start
```

### `re.sub()` — Replace Matches

```python
import re

text = "Use tabs\tnot spaces"
cleaned = re.sub(r"\s+", " ", text)  # Collapse all whitespace
print(cleaned)  # "Use tabs not spaces"

# Censor credit card numbers
masked = re.sub(r"\d{4}-\d{4}-\d{4}", "****-****-****", "Card: 1234-5678-9012-3456")
print(masked)  # "Card: ****-****-****-3456"
```

### Character Classes and Quantifiers

```python
import re

# \d = digit, \w = word char, \s = whitespace
# +  = one or more, * = zero or more, ? = zero or one
text = "Order #A123 shipped on 2024-01-15"

order_id = re.findall(r"#[A-Z]\d+", text)
print(order_id)  # ['#A123']

date = re.findall(r"\d{4}-\d{2}-\d{2}", text)
print(date)  # ['2024-01-15']
```

### Groups — Capture Parts of a Match

```python
import re

log = "ERROR 2024-01-15 Connection timeout"
match = re.match(r"(\w+)\s(\d{4}-\d{2}-\d{2})\s(.+)", log)

if match:
    level, date, message = match.groups()
    print(f"Level: {level}")    # Level: ERROR
    print(f"Date: {date}")      # Date: 2024-01-15
    print(f"Message: {message}")  # Message: Connection timeout
```

## Your Task

1. `find_emails(text)` - Extract all email addresses from text using regex
2. `extract_numbers(text)` - Find all integers in text, return as list of ints
3. `validate_phone(phone)` - Check if phone matches format XXX-XXX-XXXX
4. `replace_dates(text)` - Replace MM/DD/YYYY format with YYYY-MM-DD

## Testing
```bash
pytest exercises/18_regex_basics/test_regex.py -v
```
