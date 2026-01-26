"""
get name
print "(H)ello"
print "(G)oodbye"
print "(Q)uit"
get choice
while choice != "Q"
    if choice == "H"
        print"Hello" name
    elif choice == "G"
        print "Goodbye" name
    else
        print"Invalid choice"
    print "(H)ello"
    print "(G)oodbye"
    print "(Q)uit"
    get choice
print"finished"
"""

name = input("what is your name? ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()
print("finished")

