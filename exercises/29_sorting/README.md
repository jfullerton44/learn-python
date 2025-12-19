# Exercise 29: Sorting and Ordering

## Concept

Python provides flexible sorting with sorted() and .sort(), supporting custom keys and multiple criteria.

### Key Concepts

1. **sorted()**: Returns new sorted list
2. **.sort()**: Sorts list in place
3. **key parameter**: Custom sort function
4. **reverse**: Descending order

## AI/ML Application

- Ranking predictions by confidence
- Sorting results by multiple metrics
- Top-K selection

## Your Task

1. `sort_by_value(items)` - Sort list in ascending order
2. `sort_by_key(dict_list, key)` - Sort list of dicts by specified key
3. `sort_descending(items)` - Sort in descending order
4. `sort_by_confidence(predictions)` - Sort predictions by 'confidence' key descending
5. `sort_by_multiple_keys(items, keys)` - Sort by multiple keys using itemgetter
6. `in_place_sort(items)` - Sort list in place and return it

## Testing
```bash
pytest exercises/29_sorting/test_sorting.py -v
```
