"""Exercise 25: HTTP/APIs (Mock implementation)"""
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
    def json(self):
        return self.json_data

def mock_get_request(url):
    """Mock GET request"""
    return MockResponse({'status': 'success'}, 200)

def mock_post_request(url, data):
    """Mock POST request"""
    return MockResponse({'created': True}, 201)

def fetch_model_predictions(model_id):
    """Fetch predictions from API"""
    return {'model_id': model_id, 'predictions': [0.9, 0.1]}

def submit_training_job(config):
    """Submit training job to API"""
    return {'job_id': '12345', 'status': 'queued'}
