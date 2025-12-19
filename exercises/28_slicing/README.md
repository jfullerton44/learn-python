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
