# Exercise 57: Async Testing

## Concept

Testing asynchronous code requires special handling of event loops and async fixtures.

### Key Concepts

1. **pytest-asyncio**: Test async functions
2. **Async fixtures**: Async setup/teardown
3. **Event loop management**: Test isolation
4. **Mocking async**: AsyncMock

## AI/ML Application

- Testing async inference endpoints
- Async data loading tests
- Integration testing

## Code Examples

### Async Test Function with pytest-asyncio

```python
import pytest
import asyncio

# An async function to test
async def fetch_prediction(model_name):
    await asyncio.sleep(0.1)  # Simulate async I/O
    return {"model": model_name, "score": 0.95}

@pytest.mark.asyncio
async def test_fetch_prediction():
    result = await fetch_prediction("bert")
    assert result["model"] == "bert"
    assert result["score"] > 0.0
```

### Async Fixture

```python
import pytest
import asyncio

@pytest.fixture
async def async_database():
    """Async setup and teardown for a database connection."""
    db = {"connected": True, "data": [1, 2, 3]}
    await asyncio.sleep(0)  # Simulate async connection
    yield db
    db["connected"] = False  # Teardown

@pytest.mark.asyncio
async def test_query(async_database):
    assert async_database["connected"] is True
    assert len(async_database["data"]) == 3
```

### AsyncMock — Mocking Async Calls

```python
import pytest
from unittest.mock import AsyncMock, patch

async def call_inference_api(client, payload):
    """Calls an external async inference endpoint."""
    response = await client.post("/predict", json=payload)
    return response

@pytest.mark.asyncio
async def test_inference_api():
    mock_client = AsyncMock()
    mock_client.post.return_value = {"label": "cat", "confidence": 0.98}

    result = await call_inference_api(mock_client, {"image": "data"})
    assert result["label"] == "cat"
    mock_client.post.assert_awaited_once_with("/predict", json={"image": "data"})
```

## Your Task

1. `MLComponent` class - Async-compatible component
2. `Pipeline` class - Async pipeline
3. `create_component(name)` - Factory
4. `validate_config(config)` - Validation

## Testing
```bash
pytest exercises/57_async_testing/test_async_testing.py -v
```
