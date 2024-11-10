"""
CP1402
project
estimated: 4 hours
actual:
"""

class Project:
    """Project class"""
    def __init__(self, name, start_date, priority, completion_percentage, cost_estimate):
        """Construct instances of Project class"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.completion_percentage = completion_percentage
        self.cost_estimate = cost_estimate

    def __str__(self):
        return f'{self.name} - {self.start_date} - {self.priority} - {self.completion_percentage} - {self.cost_estimate}'

