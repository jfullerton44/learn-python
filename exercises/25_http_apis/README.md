# Exercise 25: HTTP and APIs

## Concept

Making HTTP requests to interact with web APIs. The requests library simplifies HTTP operations.

### Key Concepts

1. **GET requests**: Retrieve data from APIs
2. **POST requests**: Send data to APIs
3. **Response handling**: Status codes, JSON parsing
4. **Mock objects**: Testing without real network calls

## AI/ML Application

- Fetching model predictions from APIs
- Submitting training jobs
- Downloading datasets

## Code Examples

### Making a GET request

```python
import requests

response = requests.get("https://api.example.com/models")
print(response.status_code)  # 200
data = response.json()       # Parse JSON response body
print(data)
```

### POST request with data

```python
import requests

payload = {"model_name": "classifier", "epochs": 50}
response = requests.post("https://api.example.com/train", json=payload)
print(response.status_code)  # 201
result = response.json()
print(result["job_id"])
```

### Handling response status codes

```python
import requests

response = requests.get("https://api.example.com/predictions/42")
if response.status_code == 200:
    predictions = response.json()
elif response.status_code == 404:
    print("Model not found")
else:
    print(f"Error: {response.status_code}")
```

### Basic mock pattern for testing without network calls

```python
class FakeHTTPResponse:
    """Mimics the interface of a requests.Response for testing."""
    def __init__(self, body, code=200):
        self._body = body
        self.status_code = code
        self.ok = 200 <= code < 300

    def json(self):
        return self._body

# Use in tests instead of real HTTP calls
fake = FakeHTTPResponse({"users": ["alice", "bob"]}, 200)
print(fake.json())          # {'users': ['alice', 'bob']}
print(fake.status_code)     # 200
print(fake.ok)              # True

error_resp = FakeHTTPResponse({"error": "not found"}, 404)
print(error_resp.ok)        # False
```

## Your Task

1. `MockResponse` class - Simulate HTTP responses with json_data and status_code
2. `mock_get_request(url)` - Return mock successful GET response
3. `mock_post_request(url, data)` - Return mock successful POST response (201)
4. `fetch_model_predictions(model_id)` - Return dict with model_id and predictions
5. `submit_training_job(config)` - Return dict with job_id and status

## Testing
```bash
pytest exercises/25_http_apis/test_http.py -v
```
