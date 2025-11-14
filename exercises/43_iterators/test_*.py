import pytest
from solution import *
def test_example():
    assert example_function() == sum(range(1000))
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
