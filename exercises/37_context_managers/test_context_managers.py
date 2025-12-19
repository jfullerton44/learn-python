"""Tests for Exercise 37"""
import pytest
import tempfile
from exercise import FileManager, GPUMemoryManager, training_mode

def test_file_manager():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("test content")
        filepath = f.name

    with FileManager(filepath, 'r') as file:
        content = file.read()
        assert content == "test content"

def test_gpu_memory_manager(capsys):
    with GPUMemoryManager(0) as gpu:
        assert gpu.device_id == 0
    captured = capsys.readouterr()
    assert "Allocating GPU 0" in captured.out
    assert "Releasing GPU 0" in captured.out

def test_training_mode(capsys):
    with training_mode():
        pass
    captured = capsys.readouterr()
    assert "Entering training mode" in captured.out
    assert "Exiting training mode" in captured.out

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
