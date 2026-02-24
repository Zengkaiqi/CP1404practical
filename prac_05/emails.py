"""
email
Estimate: 15 minutes
Actual:   32 minutes
"""
user_email = input("Enter your email: ")
name_to_email = {}
while user_email != "":
    user_name = user_email.split("@")[0]
    if "."  in user_name:
        parts = user_name.split(".")
        name_to_email[" ".join(parts).title()] = user_email
    else:
        name_to_email[user_name.title()] = user_email
    user_email = input("Enter your email: ")

for key in list(name_to_email):
    email = name_to_email[key]
    print(f"Email is {email}")
    user_choice = input(f"Is your name {key} (Y/n)").lower()
    if user_choice == "n":
        new_user_name = input("Enter your name: ")
        name_to_email[new_user_name.title()] = name_to_email.pop(key)

for key in name_to_email:
    print(f"{key}({name_to_email[key]})")
