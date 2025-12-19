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
