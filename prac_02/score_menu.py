MAX_SCORE = 100
MIN_SCORE = 0
EXCELLENT_INDEX = 90
PASS_INDEX = 50
def main():
    user_score = 0
    choice = display_menu()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter your score: ",MAX_SCORE,MIN_SCORE)
            user_score = score
            print("user_score is" , user_score)
        elif choice == "P":
            score_result = determine_result(user_score)
            print(f"user score {user_score} is {score_result}")
        elif choice == "S":
            print(user_score * "*")
        else:
            print("Invalid choice")
        choice = display_menu()
    print("see you again")



def display_menu():
    print("(G)et a valid score ")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    choice = input("choose from G,P,S and Q: ").upper()
    return choice

def get_valid_score(prompt,highest_score,lowest_score):
    score = int(input(prompt))
    while score < lowest_score or score > highest_score:
        print("Enter a valid score between 0 and 100")
        score = int(input(prompt))
    return score

def determine_result(score):
    if score >= EXCELLENT_INDEX:
        print("you get prize")
        return "Excellent"
    elif score >= PASS_INDEX:
        return "Passable"
    return "Bad"

main()