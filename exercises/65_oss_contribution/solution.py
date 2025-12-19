"""
This exercise is about real-world contribution.
Students should document their OSS contribution here.
"""

class ContributionTracker:
    """Track OSS contributions"""
    def __init__(self, project_name, pr_url):
        self.project_name = project_name
        self.pr_url = pr_url
        self.status = "in_progress"

    def mark_merged(self):
        self.status = "merged"

    def get_summary(self):
        return {
            "project": self.project_name,
            "pr": self.pr_url,
            "status": self.status
        }
