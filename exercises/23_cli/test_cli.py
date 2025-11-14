"""Tests for Exercise 23"""
import pytest
from solution import parse_training_args

def test_parse_training_args():
    args = parse_training_args(['--model', 'resnet', '--epochs', '20'])
    assert args.model == 'resnet'
    assert args.epochs == 20
    assert args.lr == 0.001

def test_verbose_flag():
    args = parse_training_args(['--model', 'cnn', '--verbose'])
    assert args.verbose == True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
