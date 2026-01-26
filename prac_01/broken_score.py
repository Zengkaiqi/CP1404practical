"""
HIGHEST_SCROD = 100
MINUTE_SCROD = 0
EXCELLENT_INDEX = 90
PASS_INDEX = 50
get score
if score > HIGHEST_SCROD or score < MINUTE_SCROD
    output = "Using useful numbers"
else:
    if score >= EXCELLENT_INDEX
        output = "excellent"
    elif score >= PASS_INDEX
        output = "pass"
    else
        output = "bad"
print output
"""

HIGHEST_SCROD = 100
MINUTE_SCROD = 0
EXCELLENT_INDEX = 90
PASS_INDEX = 50
score = float(input("Type your score:"))
if score > HIGHEST_SCROD or score < MINUTE_SCROD:
    output = "Using useful numbers"
else:
    if score >= EXCELLENT_INDEX:
        output = "excellent"
    elif score >= PASS_INDEX:
        output = "pass"
    else:
        output = "bad"
print(f"score is {output} ")

