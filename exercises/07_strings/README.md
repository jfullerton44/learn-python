# Exercise 7: String Manipulation

## Concept
String methods, formatting (f-strings, format(), %), slicing, and encodings.

## AI/ML Application
- Text preprocessing for NLP
- Formatting model outputs
- Parsing logs and reports

## Code Examples

### String Methods — strip, split, join, replace
```python
raw = "  Hello, World!  "
cleaned = raw.strip()          # "Hello, World!"
lower = cleaned.lower()        # "hello, world!"

# Split a string into parts
csv_line = "alice,95,A"
parts = csv_line.split(",")    # ['alice', '95', 'A']

# Join a list into a string
words = ["hello", "world"]
sentence = " ".join(words)     # "hello world"

# Replace substrings
text = "I like cats and cats like me"
new_text = text.replace("cats", "dogs")
# "I like dogs and dogs like me"
```

### f-strings — Formatted String Literals
```python
name = "ResNet"
accuracy = 0.9523
epochs = 50

# Embed expressions directly in strings
summary = f"Model: {name}, Accuracy: {accuracy:.2%}, Epochs: {epochs}"
# "Model: ResNet, Accuracy: 95.23%, Epochs: 50"

# Expressions and padding
for i in range(1, 4):
    print(f"Epoch {i:03d}")
# Epoch 001
# Epoch 002
# Epoch 003
```

### format() Method
```python
# Positional and named placeholders
template = "Model {0} achieved {acc:.1f}% accuracy"
result = template.format("GPT", acc=92.567)
# "Model GPT achieved 92.6% accuracy"
```

### String Slicing
```python
text = "Python"
print(text[0:3])    # "Pyt"
print(text[-3:])    # "hon"
print(text[::-1])   # "nohtyP" (reversed)

# Extract parts from a structured name
model_id = "ResNet_v2.0_20240115"
model_name = model_id.split("_")[0]  # "ResNet"
```

### Encoding and Decoding
```python
text = "café"
encoded = text.encode("utf-8")   # b'caf\xc3\xa9'
decoded = encoded.decode("utf-8")  # "café"
```

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
