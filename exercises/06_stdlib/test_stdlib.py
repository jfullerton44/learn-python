"""
Tests for Exercise 6: Standard Library Essentials
"""
import pytest
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import logging
from exercise import (
    count_tokens, create_default_config, parse_log_line,
    calculate_training_time, setup_logger, parse_args_for_training
)


def test_count_tokens():
    result = count_tokens("hello world hello")
    assert result['hello'] == 2
    assert result['world'] == 1
    assert isinstance(result, Counter)


def test_create_default_config():
    config = create_default_config()
    assert isinstance(config, defaultdict)
    config['models'].append('resnet')
    assert config['models'] == ['resnet']
    assert config['nonexistent'] == []


def test_parse_log_line():
    line = "2024-01-15 10:30:45 - Training started"
    result = parse_log_line(line)
    assert result['timestamp'] == '2024-01-15 10:30:45'
    assert result['message'] == 'Training started'


def test_calculate_training_time():
    start = datetime(2024, 1, 1, 10, 0, 0)
    end = datetime(2024, 1, 1, 12, 30, 0)
    duration = calculate_training_time(start, end)
    assert isinstance(duration, timedelta)
    assert duration.total_seconds() == 9000  # 2.5 hours


def test_setup_logger():
    logger = setup_logger('test_logger', 'DEBUG')
    assert isinstance(logger, logging.Logger)
    assert logger.level == logging.DEBUG
    assert logger.name == 'test_logger'


def test_parse_args_for_training():
    args = parse_args_for_training(['--epochs', '10', '--lr', '0.001', '--model', 'resnet'])
    assert args.epochs == 10
    assert args.lr == 0.001
    assert args.model == 'resnet'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
