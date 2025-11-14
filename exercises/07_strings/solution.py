"""
Exercise 7: String Manipulation
"""
import re
from typing import Dict


def clean_text(text: str) -> str:
    """Strip whitespace, lowercase, remove extra spaces."""
    text = text.strip().lower()
    text = ' '.join(text.split())
    return text


def format_accuracy(accuracy: float, decimals: int = 2) -> str:
    """Format accuracy as percentage string."""
    return f"{accuracy * 100:.{decimals}f}%"


def parse_model_name(full_name: str) -> str:
    """Extract model name from format like 'ModelName_v1.0_20240115'."""
    return full_name.split('_')[0]


def create_report(model: str, metrics: Dict[str, float]) -> str:
    """Create formatted report using f-strings."""
    report = f"Model: {model}\n"
    for metric, value in metrics.items():
        report += f"  {metric}: {value:.4f}\n"
    return report.strip()


def tokenize_simple(text: str) -> list:
    """Split text on whitespace and punctuation."""
    return re.findall(r'\w+', text.lower())


def encode_decode_utf8(text: str) -> str:
    """Encode to UTF-8 bytes then decode back to string."""
    encoded = text.encode('utf-8')
    decoded = encoded.decode('utf-8')
    return decoded


if __name__ == "__main__":
    print(clean_text("  Hello   World  "))
    print(format_accuracy(0.9523))
    print(parse_model_name("ResNet_v1.0_20240115"))
    print(create_report("MLP", {"accuracy": 0.95, "loss": 0.05}))
    print(tokenize_simple("Hello, world! How are you?"))
    print(encode_decode_utf8("Hello 世界"))
