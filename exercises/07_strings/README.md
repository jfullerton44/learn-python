# Exercise 7: String Manipulation

## Concept
String methods, formatting (f-strings, format(), %), slicing, and encodings.

## AI/ML Application
- Text preprocessing for NLP
- Formatting model outputs
- Parsing logs and reports

## Your Task
1. `clean_text(text)` - Strip whitespace, lowercase, remove extra spaces
2. `format_accuracy(accuracy, decimals=2)` - Format as percentage (e.g., "95.23%")
3. `parse_model_name(full_name)` - Extract model name from "ModelName_v1.0_20240115"
4. `create_report(model, metrics)` - Use f-string to create formatted report
5. `tokenize_simple(text)` - Split on whitespace and punctuation
6. `encode_decode_utf8(text)` - Encode to bytes then decode back to string

## Testing
```bash
pytest exercises/07_strings/test_strings.py -v
```
