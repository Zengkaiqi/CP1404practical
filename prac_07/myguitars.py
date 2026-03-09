from prac_07.guitar import Guitar
guitars = []
with open("guitars.csv","r") as in_file:
    contents = in_file.read()
    detail = contents.split("\n")
    for guitar in detail:
        one_guitar = guitar.split(",")
        guitars.append(Guitar(one_guitar[0],int(one_guitar[1]),float(one_guitar[2].replace(",",""))))


choice = input("add a guitar?(y/n)").lower()
while choice != "n":
    name = input("name? ")
    year = int(input("year? "))
    cost = float(input("cost? "))
    guitars.append(Guitar(name, year, cost))
    with open("guitars.csv","a") as out_file:
        out_file.write("name,year,cost\n")
    choice = input("add a guitar?(y/n)").lower()
guitars.sort()
guitars.reverse()
for i, guitar in enumerate(guitars, 1):
    length = max(len(guitar.name) for guitar in guitars)
    if guitar.is_vintage():
        vintage_string = "vintage"
    elif guitar.age <= 18:
        vintage_string = "child"
    else:
        vintage_string = "adult"
    print(f"Guitar {i}: {guitar.name:>{length}} ({guitar.year}), worth ${guitar.cost:10,.2f}({vintage_string})")




