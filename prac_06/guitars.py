"""
guitars
Estimate: 15 minutes
Actual:   13 minutes
"""
from prac_06.guitar import Guitar
choice = input("add a guitar?(y/n)").lower()
guitars = []
while choice != "n":
    name = input("name? ")
    year = int(input("year? "))
    cost = float(input("cost? "))
    guitars.append(Guitar(name, year, cost))
    choice = input("add a guitar?(y/n)").lower()

for i, guitar in enumerate(guitars, 1):
    length = max(len(guitar.name) for guitar in guitars)
    if guitar.is_vintage():
        vintage_string = "vintage"
    elif guitar.age <= 18:
        vintage_string = "child"
    else:
        vintage_string = "adult"
    print(f"Guitar {i}: {guitar.name:>{length}} ({guitar.year}), worth ${guitar.cost:10,.2f}({vintage_string})")