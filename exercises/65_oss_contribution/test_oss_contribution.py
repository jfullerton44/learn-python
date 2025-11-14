"""Tests for OSS contribution tracking"""
import pytest
from solution import ContributionTracker

def test_contribution_tracker():
    tracker = ContributionTracker("pytorch", "https://github.com/pytorch/pytorch/pull/12345")
    assert tracker.status == "in_progress"
    tracker.mark_merged()
    assert tracker.status == "merged"
    summary = tracker.get_summary()
    assert "pytorch" in summary["project"]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
