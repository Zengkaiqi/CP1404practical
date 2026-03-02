"""
guitar
Estimate: 20 minutes
Actual:   14 minutes
"""
import datetime
VINTAGE_INDEX = 50
class Guitar:
    def __init__(self,name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = datetime.datetime.now().year - self.year

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return self.age

    def is_vintage(self):
        return self.age >= VINTAGE_INDEX
