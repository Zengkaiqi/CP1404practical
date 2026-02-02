import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""I try 5 times"""
#What did you see on line 1?
"""9  , 19  ,7  ,  12   ,  9"""
#What was the smallest number you could have seen, what was the largest?
"""7 is the smallest number and 19 is the largest number"""

#What did you see on line 2?
"""7  , 5   ,7   ,  3  ,  7"""
#What was the smallest number you could have seen, what was the largest?
"""3 is the smallest number and 7 is the largest number"""
#Could line 2 have produced a 4?
"""No , it only can be 3,5,7,9"""

#What did you see on line 3?
"""4.595319143617266  ,  5.0674779464363855   ,2.9005883982549756   ,  3.624713804063006   ,   4.280016702476268"""
#What was the smallest number you could have seen, what was the largest?
"""2.9005883982549756 is the smallest number and 5.0674779464363855 is the largest number"""
#Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1,100))