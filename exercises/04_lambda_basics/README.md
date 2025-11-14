# Exercise 4: Lambda Functions and Basic Functional Programming

## Concept

Lambda functions are anonymous, single-expression functions. Combined with map(), filter(), reduce(), and sorted(), they enable functional programming patterns.

## AI/ML Application

- Filtering datasets
- Transforming features
- Sorting predictions by confidence
- Aggregating metrics

## Your Task

1. `apply_activation(values, activation_name)` - Use lambda with map() to apply activation:
   - "relu": max(0, x)
   - "sigmoid": 1 / (1 + e^(-x))
2. `filter_by_threshold(predictions, threshold)` - Filter predictions >= threshold
3. `sort_by_confidence(predictions)` - Sort list of dicts by 'confidence' key (descending)
4. `compute_total_loss(losses)` - Use reduce() to sum losses
5. `create_scaler(factor)` - Return lambda that multiplies input by factor

## Testing
```bash
pytest exercises/04_lambda_basics/test_lambda.py -v
```
