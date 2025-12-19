import pytest
from exercise import *
def test_worker():
    assert worker_function() == "completed"
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
