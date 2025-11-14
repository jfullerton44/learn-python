# Exercise 8: Basic Data Structures

## Concept
Master lists, tuples, sets, dicts - when to use each, trade-offs.

## AI/ML Application
- Storing predictions and labels
- Managing hyperparameters
- Caching computed results
- Deduplication of data

## Your Task
1. `store_predictions(predictions, labels)` - Return list of tuples (pred, label)
2. `manage_hyperparams()` - Return dict with nested structure
3. `deduplicate_samples(samples)` - Use set to remove duplicates, return list
4. `cache_results(func, args_list)` - Cache function results in dict
5. `implement_stack()` - Return list with push/pop operations
6. `implement_queue()` - Use collections.deque for queue operations

## Testing
```bash
pytest exercises/08_data_structures/test_data_structures.py -v
```
