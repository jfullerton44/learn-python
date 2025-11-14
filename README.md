# Learn Python for AI Engineers

A comprehensive, hands-on Python learning repository designed to take you from intermediate to expert-level Python, with a focus on AI/ML engineering.

## 📚 What's Included

**65 Progressive Exercises** organized into 11 phases:
- **Phase 0** (Exercises 1-35): Python Fundamentals
- **Phase 1** (Exercises 36-39): Advanced Python Fundamentals
- **Phase 2** (Exercises 40-43): Performance and Optimization
- **Phase 3** (Exercises 44-46): Concurrency and Parallelism
- **Phase 4** (Exercises 47-48): Advanced Type Systems
- **Phase 5** (Exercises 49-50): Functional Programming
- **Phase 6** (Exercises 51-53): Design Patterns for AI
- **Phase 7** (Exercises 54-55): Advanced Data Structures
- **Phase 8** (Exercises 56-57): Testing and Quality
- **Phase 9** (Exercises 58-60): Real-World AI Patterns
- **Phase 10** (Exercises 61-63): Advanced Topics
- **Capstone** (Exercises 64-65): Final Projects

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic Python knowledge (variables, functions, loops)

### Setup

1. **Clone this repository**
```bash
git clone <repository-url>
cd learn-python
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📖 How to Use

### Structure
Each exercise contains:
- `README.md` - Concept explanation and task description
- `solution.py` - Your implementation (starter code provided)
- `test_*.py` - Test suite to validate your solution

### Workflow

1. **Read the README**
```bash
cd exercises/01_oop_basics
cat README.md
```

2. **Implement the solution**
Edit `solution.py` to complete the tasks

3. **Run the tests**
```bash
pytest test_oop.py -v
```

4. **Iterate**
Fix any failing tests and improve your solution

### Running Tests

```bash
# Run tests for a specific exercise
pytest exercises/01_oop_basics/test_oop.py -v

# Run all tests in a phase
pytest exercises/{01..10}*/test_*.py -v

# Run all tests
pytest exercises/ -v

# Run with coverage
pytest exercises/ --cov=exercises --cov-report=html
```

## 📋 Learning Path

### For Beginners
Start with **Phase 0** (Exercises 1-35) to build a strong foundation.

### For Intermediate Developers
- Review Phase 0 quickly (1-2 weeks)
- Focus on Phases 1-10 for advanced concepts

### For Experienced Developers
- Jump directly to areas of interest
- Complete the Capstone projects (64-65)

## 📊 Progress Tracking

Use this checklist to track your progress:

- [ ] **Phase 0**: Python Fundamentals (1-35)
- [ ] **Phase 1**: Advanced Python Fundamentals (36-39)
- [ ] **Phase 2**: Performance and Optimization (40-43)
- [ ] **Phase 3**: Concurrency and Parallelism (44-46)
- [ ] **Phase 4**: Advanced Type Systems (47-48)
- [ ] **Phase 5**: Functional Programming (49-50)
- [ ] **Phase 6**: Design Patterns for AI (51-53)
- [ ] **Phase 7**: Advanced Data Structures (54-55)
- [ ] **Phase 8**: Testing and Quality (56-57)
- [ ] **Phase 9**: Real-World AI Patterns (58-60)
- [ ] **Phase 10**: Advanced Topics (61-63)
- [ ] **Capstone**: Final Projects (64-65)

## 🎯 Learning Objectives

By completing this curriculum, you will:
- ✅ Master Python from fundamentals through advanced concepts
- ✅ Write production-grade Python code for AI systems
- ✅ Optimize critical performance bottlenecks
- ✅ Design scalable ML infrastructure
- ✅ Debug complex concurrent and distributed systems
- ✅ Work confidently with ML libraries (NumPy, Pandas, PyTorch/TensorFlow)
- ✅ Build complete ML systems from scratch
- ✅ Contribute to major Python AI projects

## 📚 Additional Resources

Each exercise README includes:
- Detailed concept explanations
- Links to official Python documentation
- Real-world AI/ML examples
- Common pitfalls to avoid

## 🤝 Contributing

Found an issue or want to add an exercise? Contributions are welcome!

## 📝 License

This educational repository is provided as-is for learning purposes.

## 🎓 Next Steps

1. Start with Exercise 1: Object-Oriented Programming Basics
2. Work through exercises sequentially
3. Apply concepts to your own AI/ML projects
4. Complete the capstone project to showcase your skills

**Happy Learning! 🚀**

---

## Quick Reference

### Useful Commands
```bash
# List all exercises
ls exercises/

# Count completed exercises
find exercises/ -name "solution.py" -type f | wc -l

# Run specific phase tests
pytest exercises/{01..35}*/test_*.py  # Phase 0
pytest exercises/{36..39}*/test_*.py  # Phase 1

# Check Python version
python --version

# Activate virtual environment
source venv/bin/activate
```

### Need Help?
- Check the LEARNING_PLAN.md for detailed curriculum
- Review PREREQUISITE_TOPICS.md for foundational topics
- Run `pytest --help` for testing options

Start your Python mastery journey today! 🎉
