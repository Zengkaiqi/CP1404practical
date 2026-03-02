"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

MAX_SCORE = 100
MIN_SCORE = 0
EXCELLENT_INDEX = 90
PASS_INDEX = 50
def main():
    score = get_valid_score("Enter your score: ",MAX_SCORE,MIN_SCORE)
    result = determine_result(score)
    random_score = random.randint(MIN_SCORE,MAX_SCORE)
    random_result =determine_result(random_score)
    print (f"The result of user input {score} is {result},\nThe random score {random_score} = {random_result}")

def get_valid_score(prompt,highest,lowest):
    score = float(input(prompt))
    while score < lowest or score > highest:
        print("Invalid score")
        score = float(input(prompt))
    return score

def determine_result(score):
    if score >= EXCELLENT_INDEX:
        print("you get prize")
        return "Excellent"
    elif score >= PASS_INDEX :
        return "Passable"
    return "Bad"

main()