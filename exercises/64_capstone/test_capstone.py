"""Tests for capstone project"""
import pytest
from exercise import Tensor, Model, Trainer, DataLoader

def test_tensor():
    t = Tensor([1, 2, 3], requires_grad=True)
    assert t.data == [1, 2, 3]
    t.backward()
    assert t.grad == 1.0

def test_model():
    model = Model()
    output = model.forward([1, 2, 3])
    assert output == [1, 2, 3]

def test_trainer():
    model = Model()
    trainer = Trainer(model, None)
    trainer.train(epochs=1)

def test_dataloader():
    dataset = list(range(100))
    loader = DataLoader(dataset, batch_size=10)
    assert len(loader) == 10
    batches = list(loader)
    assert len(batches) == 10

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
