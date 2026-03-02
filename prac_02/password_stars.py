def main():
    password_length = determine_password_length("Enter your password: ",10,5)
    outcome = display_output(password_length,"😃")
    print(outcome)

def determine_password_length(prompt,highest,lowest):
    password_length = len(input(prompt))
    while password_length > highest or password_length < lowest:
        password_length = len(input(prompt))
    return password_length

def display_output(password_length,char = "*"):
    return f"your password is {password_length * char}"
main()