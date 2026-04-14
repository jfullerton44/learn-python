# Exercise 56: Advanced Testing

## Concept

Advanced testing techniques for robust ML codebases including mocking, fixtures, and property-based testing.

### Key Concepts

1. **Mocking**: Isolate units under test
2. **Fixtures**: Reusable test setup
3. **Parametrization**: Test multiple inputs
4. **Property-based testing**: Generate test cases

## AI/ML Application

- Testing model components in isolation
- Data pipeline testing
- Reproducible test environments

## Code Examples

### Mocking — Isolate External Dependencies

```python
from unittest.mock import patch, MagicMock

# Suppose fetch_data calls an external API
def fetch_data(url):
    import requests
    return requests.get(url).json()

def get_user_count(url):
    data = fetch_data(url)
    return len(data["users"])

# Mock fetch_data so the test never hits the network
with patch("__main__.fetch_data", return_value={"users": ["a", "b", "c"]}):
    assert get_user_count("http://fake.url") == 3
```

### Fixtures — Reusable Test Setup

```python
import pytest

@pytest.fixture
def sample_dataset():
    """Provide a reusable dataset for multiple tests."""
    return [1.0, 2.0, 3.0, 4.0, 5.0]

def test_mean(sample_dataset):
    assert sum(sample_dataset) / len(sample_dataset) == 3.0

def test_length(sample_dataset):
    assert len(sample_dataset) == 5
```

### Parametrize — Test Multiple Inputs Concisely

```python
import pytest

def relu(x):
    return max(0, x)

@pytest.mark.parametrize("input_val, expected", [
    (5, 5),
    (-3, 0),
    (0, 0),
    (0.5, 0.5),
])
def test_relu(input_val, expected):
    assert relu(input_val) == expected
```

### Property-Based Testing Concept

```python
# Property-based testing generates random inputs to verify invariants.
# Uses the 'hypothesis' library.
from hypothesis import given
from hypothesis import strategies as st

def sort_list(lst):
    return sorted(lst)

@given(st.lists(st.integers()))
def test_sort_is_idempotent(lst):
    """Sorting twice gives the same result as sorting once."""
    assert sort_list(sort_list(lst)) == sort_list(lst)

@given(st.lists(st.integers()))
def test_sort_preserves_length(lst):
    assert len(sort_list(lst)) == len(lst)
```

## Your Task

1. `MLComponent` class - Testable component
2. `Pipeline` class - Pipeline with test hooks
3. `create_component(name)` - Factory
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/56_testing/test_testing.py -v
```
