"""Tests for Exercise 22"""
import pytest
import logging
from exercise import setup_basic_logger, log_training_progress, log_error

def test_setup_basic_logger():
    logger = setup_basic_logger('test')
    assert isinstance(logger, logging.Logger)
    assert logger.level == logging.INFO

def test_log_training_progress(caplog):
    logger = setup_basic_logger('train')
    log_training_progress(logger, 1, 0.5)
    # Logging test passes if no exception

def test_log_error(caplog):
    logger = setup_basic_logger('error_test')
    log_error(logger, "Test error")
    # Logging test passes if no exception

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
