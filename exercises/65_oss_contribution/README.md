# Exercise 65: Open Source Contribution

## Goal
Make a meaningful contribution to an open-source AI project (PyTorch, HuggingFace, Scikit-learn, etc.)

## Steps
1. Choose a project
2. Set up development environment
3. Find an issue to work on
4. Submit a pull request
5. Document your contribution

## Code Examples

### Git Fork-and-Branch Workflow

```bash
# 1. Fork the project on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/project.git
cd project

# 2. Add the original repo as "upstream"
git remote add upstream https://github.com/ORIGINAL_OWNER/project.git

# 3. Create a feature branch from up-to-date main
git fetch upstream
git checkout -b fix-data-loader upstream/main

# 4. Make changes, then commit and push
git add src/data_loader.py tests/test_data_loader.py
git commit -m "Fix off-by-one error in batch iterator"
git push origin fix-data-loader

# 5. Open a Pull Request from your fork's branch to upstream/main
```

### Writing a Good Commit Message

```
fix: correct off-by-one error in DataLoader batch slicing

The batch iterator was skipping the last partial batch when the dataset
size was not evenly divisible by the batch size. This caused up to
(batch_size - 1) samples to be silently dropped each epoch.

- Changed range stop from `len(data) - batch_size` to `len(data)`
- Added test case for non-divisible dataset sizes

Fixes #142
```

### Example Pull Request Description

```markdown
## Summary
Fix off-by-one error in `DataLoader.batch_iterator()` that silently
dropped the last partial batch (#142).

## Changes
- `src/data_loader.py`: Fixed loop boundary in `batch_iterator()`
- `tests/test_data_loader.py`: Added test for partial final batch

## Testing
- All existing tests pass (`pytest tests/ -v`)
- Added new test: `test_partial_last_batch`

## Checklist
- [x] Tests added for the bug fix
- [x] Documentation updated (docstring)
- [x] Ran linter (`flake8`) with no new warnings
```

### Example: Writing a Bug Fix with Tests

```python
# Before your fix (the bug):
def batch_iterator(data, batch_size):
    """Yields batches — but drops the last partial batch!"""
    for i in range(0, len(data) - batch_size, batch_size):
        yield data[i:i + batch_size]

# After your fix:
def batch_iterator(data, batch_size):
    """Yields batches, including the final partial batch."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# Always add a test for the fix:
def test_partial_last_batch():
    data = [1, 2, 3, 4, 5]
    batches = list(batch_iterator(data, batch_size=2))
    assert batches == [[1, 2], [3, 4], [5]]  # last partial batch included
```

### Finding Issues to Work On

```bash
# Search for beginner-friendly issues on GitHub
# Look for labels: "good first issue", "help wanted", "beginner"

# Using the GitHub CLI:
gh issue list --repo pytorch/pytorch --label "good first issue" --state open

# Or browse: https://github.com/pytorch/pytorch/labels/good%20first%20issue
```

## Documentation
Create a detailed report in this directory documenting:
- Project chosen
- Issue/feature worked on  
- Technical challenges
- Code changes made
- Link to PR
- Lessons learned

## Deliverable
`contribution_report.md` with full documentation of your contribution.
