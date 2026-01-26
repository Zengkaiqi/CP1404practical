"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

max_score = 100
min_score = 0
def main():
    score = get_valid_score("Enter your score: ",max_score,min_score)
    result = determine_result(score)
    random_score = random.randint(min_score,max_score)
    random_result =determine_result(random_score)
    print (f"The result of user input {score}:{result},the random score {random_score}:{random_result}")

def get_valid_score(prompt,highest,lowest):
    score = float(input(prompt))
    while score < lowest or score > highest:
        print("Invalid score")
        score = float(input(prompt))
    return score

def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    return "Bad"

main()