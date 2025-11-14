"""
Tests for Exercise 7: String Manipulation
"""
import pytest
from solution import (
    clean_text, format_accuracy, parse_model_name,
    create_report, tokenize_simple, encode_decode_utf8
)


def test_clean_text():
    assert clean_text("  Hello   World  ") == "hello world"
    assert clean_text("Test  String") == "test string"
    assert clean_text("  UPPERCASE  ") == "uppercase"


def test_format_accuracy():
    assert format_accuracy(0.9523) == "95.23%"
    assert format_accuracy(0.9, 1) == "90.0%"
    assert format_accuracy(1.0) == "100.00%"


def test_parse_model_name():
    assert parse_model_name("ResNet_v1.0_20240115") == "ResNet"
    assert parse_model_name("BERT_v2.0_final") == "BERT"


def test_create_report():
    report = create_report("MLP", {"accuracy": 0.95, "loss": 0.05})
    assert "Model: MLP" in report
    assert "accuracy: 0.9500" in report
    assert "loss: 0.0500" in report


def test_tokenize_simple():
    tokens = tokenize_simple("Hello, world! How are you?")
    assert tokens == ["hello", "world", "how", "are", "you"]


def test_encode_decode_utf8():
    assert encode_decode_utf8("Hello") == "Hello"
    assert encode_decode_utf8("Hello 世界") == "Hello 世界"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
