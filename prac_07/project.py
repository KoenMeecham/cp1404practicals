"""
CP1402
project
estimated: 4 hours
actual:
"""
import datetime
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
        """String representation of Project class"""
        return f'{self.name} - {self.start_date} - {self.priority} - {self.completion_percentage} - {self.cost_estimate}'

    def __repr__(self):
        """List representation of Project class"""
        return str(self)

    def is_complete(self):
        """Return True if Project is complete (100%)"""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """Return True if one priority is greater than the other is less than other (sorts by higher priority)"""
        return self.priority > other.priority

    def __gt__(self, other):
        """Return true if one date is greater than the other"""
        return self.start_date > other.start_date


