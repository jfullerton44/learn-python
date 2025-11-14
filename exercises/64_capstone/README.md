# Exercise 64: Build a Mini ML Framework

## Project Goal
Build a lightweight ML framework combining all learned concepts.

## Requirements
1. Auto-differentiation engine
2. Configurable training loops with callbacks  
3. Custom dataset loaders with caching
4. Async inference server
5. Distributed training coordinator
6. Comprehensive test suite

## Structure
```
64_capstone/
├── README.md
├── framework/
│   ├── __init__.py
│   ├── autograd.py
│   ├── training.py
│   ├── data.py
│   └── server.py
├── tests/
│   └── test_framework.py
└── examples/
    └── train_model.py
```

## Testing
```bash
pytest exercises/64_capstone/tests/ -v
```
