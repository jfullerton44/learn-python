# Python Expert Learning Plan for AI Engineers

This repository contains a progressive series of exercises designed to take you from intermediate to expert-level Python, with a focus on skills critical for AI/ML engineering.

## Learning Path Overview

### Phase 1: Advanced Python Fundamentals (Weeks 1-2)

#### Exercise 1: Advanced Decorators and Metaprogramming
- **Concept**: Function/class decorators, decorator factories, wrapping with functools
- **AI Application**: Creating training loop decorators, timing/profiling ML experiments
- **Deliverables**:
  - `exercises/01_decorators/README.md` - Concept explanation
  - `exercises/01_decorators/solution.py` - Implementation
  - `exercises/01_decorators/test_decorators.py` - Validation tests

#### Exercise 2: Context Managers and Resource Management
- **Concept**: `__enter__`/`__exit__`, contextlib, resource cleanup
- **AI Application**: Managing GPU memory, model checkpointing, dataset loading
- **Deliverables**:
  - `exercises/02_context_managers/README.md`
  - `exercises/02_context_managers/solution.py`
  - `exercises/02_context_managers/test_context_managers.py`

#### Exercise 3: Metaclasses and Class Customization
- **Concept**: Metaclasses, `__init_subclass__`, class factories
- **AI Application**: Auto-registering model architectures, config validation
- **Deliverables**:
  - `exercises/03_metaclasses/README.md`
  - `exercises/03_metaclasses/solution.py`
  - `exercises/03_metaclasses/test_metaclasses.py`

#### Exercise 4: Descriptors and Properties
- **Concept**: Data descriptors, non-data descriptors, property protocols
- **AI Application**: Lazy-loading model weights, validated hyperparameters
- **Deliverables**:
  - `exercises/04_descriptors/README.md`
  - `exercises/04_descriptors/solution.py`
  - `exercises/04_descriptors/test_descriptors.py`

### Phase 2: Performance and Optimization (Weeks 3-4)

#### Exercise 5: Profiling and Performance Analysis
- **Concept**: cProfile, line_profiler, memory_profiler, timeit
- **AI Application**: Identifying bottlenecks in data preprocessing pipelines
- **Deliverables**:
  - `exercises/05_profiling/README.md`
  - `exercises/05_profiling/solution.py`
  - `exercises/05_profiling/test_profiling.py`

#### Exercise 6: NumPy Vectorization and Broadcasting
- **Concept**: Advanced indexing, broadcasting rules, stride tricks, einsum
- **AI Application**: Efficient tensor operations without loops
- **Deliverables**:
  - `exercises/06_numpy_advanced/README.md`
  - `exercises/06_numpy_advanced/solution.py`
  - `exercises/06_numpy_advanced/test_numpy.py`

#### Exercise 7: Memory Management and Optimization
- **Concept**: `__slots__`, generators vs lists, memory views, gc module
- **AI Application**: Handling large datasets, reducing memory footprint
- **Deliverables**:
  - `exercises/07_memory/README.md`
  - `exercises/07_memory/solution.py`
  - `exercises/07_memory/test_memory.py`

#### Exercise 8: Iterator Protocols and Generators
- **Concept**: Iterators, generators, yield from, itertools mastery
- **AI Application**: Streaming data loading, infinite data generators
- **Deliverables**:
  - `exercises/08_iterators/README.md`
  - `exercises/08_iterators/solution.py`
  - `exercises/08_iterators/test_iterators.py`

### Phase 3: Concurrency and Parallelism (Weeks 5-6)

#### Exercise 9: Multithreading and the GIL
- **Concept**: Threading, thread pools, locks, GIL implications
- **AI Application**: Parallel I/O for data loading, concurrent API calls
- **Deliverables**:
  - `exercises/09_threading/README.md`
  - `exercises/09_threading/solution.py`
  - `exercises/09_threading/test_threading.py`

#### Exercise 10: Multiprocessing and Process Pools
- **Concept**: Process pools, shared memory, Queue, Manager
- **AI Application**: Parallel data preprocessing, distributed training coordination
- **Deliverables**:
  - `exercises/10_multiprocessing/README.md`
  - `exercises/10_multiprocessing/solution.py`
  - `exercises/10_multiprocessing/test_multiprocessing.py`

#### Exercise 11: Async/Await and Asyncio
- **Concept**: Coroutines, event loop, async context managers, aiohttp
- **AI Application**: Async data fetching, concurrent model inference APIs
- **Deliverables**:
  - `exercises/11_asyncio/README.md`
  - `exercises/11_asyncio/solution.py`
  - `exercises/11_asyncio/test_asyncio.py`

### Phase 4: Advanced Type Systems (Week 7)

#### Exercise 12: Advanced Type Hints
- **Concept**: Generics, Protocol, TypeVar, ParamSpec, Literal
- **AI Application**: Type-safe model configs, generic dataset classes
- **Deliverables**:
  - `exercises/12_typing/README.md`
  - `exercises/12_typing/solution.py`
  - `exercises/12_typing/test_typing.py`

#### Exercise 13: Runtime Type Validation
- **Concept**: Pydantic, dataclasses, attrs, validation decorators
- **AI Application**: Validating experiment configs, API request/response
- **Deliverables**:
  - `exercises/13_validation/README.md`
  - `exercises/13_validation/solution.py`
  - `exercises/13_validation/test_validation.py`

### Phase 5: Functional Programming (Week 8)

#### Exercise 14: Functional Programming Patterns
- **Concept**: map/filter/reduce, partial application, composition, immutability
- **AI Application**: Data transformation pipelines, pure preprocessing functions
- **Deliverables**:
  - `exercises/14_functional/README.md`
  - `exercises/14_functional/solution.py`
  - `exercises/14_functional/test_functional.py`

#### Exercise 15: Closures and Currying
- **Concept**: Closures, currying, function factories
- **AI Application**: Creating parameterized loss functions, custom optimizers
- **Deliverables**:
  - `exercises/15_closures/README.md`
  - `exercises/15_closures/solution.py`
  - `exercises/15_closures/test_closures.py`

### Phase 6: Design Patterns for AI (Weeks 9-10)

#### Exercise 16: Factory and Builder Patterns
- **Concept**: Abstract factories, builders for complex objects
- **AI Application**: Model factories, experiment builders
- **Deliverables**:
  - `exercises/16_factory_builder/README.md`
  - `exercises/16_factory_builder/solution.py`
  - `exercises/16_factory_builder/test_patterns.py`

#### Exercise 17: Strategy and Observer Patterns
- **Concept**: Strategy pattern, observer/pub-sub
- **AI Application**: Pluggable training strategies, training callbacks
- **Deliverables**:
  - `exercises/17_strategy_observer/README.md`
  - `exercises/17_strategy_observer/solution.py`
  - `exercises/17_strategy_observer/test_patterns.py`

#### Exercise 18: Pipeline and Chain of Responsibility
- **Concept**: Pipeline pattern, chaining operations
- **AI Application**: Data preprocessing pipelines, model ensemble chains
- **Deliverables**:
  - `exercises/18_pipeline/README.md`
  - `exercises/18_pipeline/solution.py`
  - `exercises/18_pipeline/test_pipeline.py`

### Phase 7: Advanced Data Structures (Week 11)

#### Exercise 19: Custom Collections and ABCs
- **Concept**: Abstract Base Classes, MutableMapping, Sequence protocols
- **AI Application**: Custom dataset containers, config dictionaries
- **Deliverables**:
  - `exercises/19_collections/README.md`
  - `exercises/19_collections/solution.py`
  - `exercises/19_collections/test_collections.py`

#### Exercise 20: Trees, Graphs, and Advanced Algorithms
- **Concept**: Implementing efficient tree/graph structures, algorithms
- **AI Application**: Neural architecture search, computation graphs
- **Deliverables**:
  - `exercises/20_algorithms/README.md`
  - `exercises/20_algorithms/solution.py`
  - `exercises/20_algorithms/test_algorithms.py`

### Phase 8: Testing and Quality (Week 12)

#### Exercise 21: Advanced Testing with Pytest
- **Concept**: Fixtures, parametrize, mocking, hypothesis testing
- **AI Application**: Testing ML pipelines, property-based testing for data
- **Deliverables**:
  - `exercises/21_testing/README.md`
  - `exercises/21_testing/solution.py`
  - `exercises/21_testing/test_testing.py`

#### Exercise 22: Testing Async Code and Concurrent Systems
- **Concept**: pytest-asyncio, testing race conditions, mocking async
- **AI Application**: Testing async inference endpoints, concurrent data loaders
- **Deliverables**:
  - `exercises/22_async_testing/README.md`
  - `exercises/22_async_testing/solution.py`
  - `exercises/22_async_testing/test_async.py`

### Phase 9: Real-World AI Patterns (Weeks 13-14)

#### Exercise 23: Configuration Management Systems
- **Concept**: Hydra-style configs, environment management, secrets
- **AI Application**: Managing complex ML experiments with multiple configs
- **Deliverables**:
  - `exercises/23_config_systems/README.md`
  - `exercises/23_config_systems/solution.py`
  - `exercises/23_config_systems/test_config.py`

#### Exercise 24: Custom Dataset Iterables
- **Concept**: PyTorch-style datasets, lazy loading, caching strategies
- **AI Application**: Efficient data loading for large-scale training
- **Deliverables**:
  - `exercises/24_dataset_patterns/README.md`
  - `exercises/24_dataset_patterns/solution.py`
  - `exercises/24_dataset_patterns/test_dataset.py`

#### Exercise 25: Distributed Computing Primitives
- **Concept**: Ray/distributed concepts, task graphs, futures
- **AI Application**: Distributed hyperparameter tuning, parallel evaluation
- **Deliverables**:
  - `exercises/25_distributed/README.md`
  - `exercises/25_distributed/solution.py`
  - `exercises/25_distributed/test_distributed.py`

### Phase 10: Advanced Topics (Weeks 15-16)

#### Exercise 26: Custom C Extensions and Cython
- **Concept**: ctypes, cffi, basic Cython for performance
- **AI Application**: Accelerating critical preprocessing bottlenecks
- **Deliverables**:
  - `exercises/26_c_extensions/README.md`
  - `exercises/26_c_extensions/solution.py`
  - `exercises/26_c_extensions/test_extensions.py`

#### Exercise 27: Debugging and Introspection
- **Concept**: pdb++, inspect module, stack traces, post-mortem debugging
- **AI Application**: Debugging training failures, inspecting model internals
- **Deliverables**:
  - `exercises/27_debugging/README.md`
  - `exercises/27_debugging/solution.py`
  - `exercises/27_debugging/test_debugging.py`

#### Exercise 28: Package Structure and Distribution
- **Concept**: setup.py, pyproject.toml, entry points, versioning
- **AI Application**: Creating reusable ML libraries, tool distribution
- **Deliverables**:
  - `exercises/28_packaging/README.md`
  - `exercises/28_packaging/solution.py`
  - `exercises/28_packaging/test_packaging.py`

### Capstone Project (Weeks 17-18)

#### Exercise 29: Build a Mini ML Framework
- **Concept**: Combining all learned concepts
- **Challenge**: Build a lightweight ML framework with:
  - Auto-differentiation engine
  - Configurable training loops with callbacks
  - Custom dataset loaders with caching
  - Async inference server
  - Distributed training coordinator
  - Comprehensive test suite
- **Deliverables**:
  - `exercises/29_capstone/README.md`
  - `exercises/29_capstone/` (full project structure)
  - `exercises/29_capstone/tests/`

#### Exercise 30: Contribute to an Open Source AI Project
- **Concept**: Real-world application of all skills
- **Challenge**: Make a meaningful contribution to PyTorch, HuggingFace, or similar
- **Deliverables**:
  - `exercises/30_oss_contribution/README.md` (documenting the contribution)
  - Link to actual PR/contribution

---

## Repository Structure

```
learn-python/
├── LEARNING_PLAN.md (this file)
├── README.md (repo overview)
├── requirements.txt (dependencies)
├── exercises/
│   ├── 01_decorators/
│   │   ├── README.md
│   │   ├── solution.py
│   │   └── test_decorators.py
│   ├── 02_context_managers/
│   │   └── ...
│   └── ...
└── utils/ (shared utilities)
```

## How to Use This Plan

1. **Sequential Learning**: Complete exercises in order, as later ones build on earlier concepts
2. **Test-Driven**: Always run tests to validate your solutions
3. **Read First**: Study the README.md for each exercise before coding
4. **Iterate**: Solutions can be revisited and improved
5. **Apply**: After each phase, try applying concepts to your actual AI work

## Testing Your Solutions

Each exercise includes pytest tests:
```bash
# Run specific exercise tests
pytest exercises/01_decorators/test_decorators.py -v

# Run all tests
pytest exercises/ -v

# Run with coverage
pytest exercises/ --cov=exercises --cov-report=html
```

## Time Commitment

- **Estimated**: 16-18 weeks at 5-10 hours/week
- **Flexible**: Adjust pace based on your schedule and existing knowledge
- **Practice**: Additional time recommended for applying concepts to real projects

## Success Metrics

By completing this plan, you should be able to:
- Write production-grade Python code for AI systems
- Optimize critical performance bottlenecks
- Design scalable ML infrastructure
- Debug complex concurrent and distributed systems
- Contribute meaningfully to major Python AI projects
- Make informed decisions about architecture and tooling

## Additional Resources

Each exercise README will include:
- Concept explanations with examples
- Links to official Python docs
- Recommended reading/videos
- Common pitfalls to avoid
- Real-world AI examples

---

**Ready to start?** Begin with Exercise 1: Advanced Decorators!
