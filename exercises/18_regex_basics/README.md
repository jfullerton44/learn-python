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

## Your Task

1. `find_emails(text)` - Extract all email addresses from text using regex
2. `extract_numbers(text)` - Find all integers in text, return as list of ints
3. `validate_phone(phone)` - Check if phone matches format XXX-XXX-XXXX
4. `replace_dates(text)` - Replace MM/DD/YYYY format with YYYY-MM-DD

## Testing
```bash
pytest exercises/18_regex_basics/test_regex.py -v
```
