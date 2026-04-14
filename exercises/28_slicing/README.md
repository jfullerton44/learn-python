# Exercise 28: Advanced Slicing

## Concept

Python's slicing syntax [start:stop:step] provides powerful ways to extract and manipulate sequences.

### Key Concepts

1. **Step slicing**: `[::n]` for every nth element
2. **Negative indices**: Access from end of sequence
3. **Reverse**: `[::-1]` reverses sequences
4. **Slice objects**: Reusable slice definitions

## AI/ML Application

- Batch processing of data
- Data augmentation (reversing sequences)
- Extracting train/validation splits

## Code Examples

### Basic slicing with `[start:stop]`

```python
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[1:4])   # [20, 30, 40] — indices 1, 2, 3
print(numbers[:3])    # [10, 20, 30] — first 3 elements
print(numbers[4:])    # [50, 60, 70] — from index 4 to end
```

### Step slicing with `[::n]` for every nth element

```python
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data[::2])    # [0, 2, 4, 6, 8] — every 2nd element
print(data[::3])    # [0, 3, 6, 9]    — every 3rd element
print(data[1::2])   # [1, 3, 5, 7, 9] — odd-indexed elements
```

### Negative indices and reversing

```python
items = ["a", "b", "c", "d", "e"]
print(items[-1])     # 'e'          — last element
print(items[-3:])    # ['c', 'd', 'e'] — last 3 elements
print(items[::-1])   # ['e', 'd', 'c', 'b', 'a'] — reversed
```

### Using `slice()` objects for reusable slices

```python
# Create a reusable slice object
batch_slice = slice(0, 32)     # First 32 items (like a batch)
step_slice = slice(None, None, 2)  # Every other item

data = list(range(100))
batch = data[batch_slice]       # [0, 1, 2, ..., 31]
sampled = data[step_slice]      # [0, 2, 4, ..., 98]
print(len(batch))    # 32
print(len(sampled))  # 50
```

## Your Task

1. `get_every_nth(items, n)` - Return every nth element using step slicing
2. `reverse_list(items)` - Reverse list using [::-1]
3. `get_last_n(items, n)` - Get last n items using negative indexing
4. `get_middle_section(items, start_frac, end_frac)` - Get middle portion by fractions
5. `create_slice_object(start, stop, step)` - Create a slice object
6. `apply_slice(items, slice_obj)` - Apply slice object to items

## Testing
```bash
pytest exercises/28_slicing/test_slicing.py -v
```
