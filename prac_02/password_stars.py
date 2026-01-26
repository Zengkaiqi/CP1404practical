def main():
    password_length = determine_password_length("Enter your password: ",10,5)
    print(f"your password is {password_length * "*"}")

def determine_password_length(prompt,highest,lowest):
    password_length = len(input(prompt))
    while password_length > highest or password_length < lowest:
        password_length = len(input(prompt))
    return password_length

main()