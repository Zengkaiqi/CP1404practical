"""
guitar test
Estimate: 5 minutes
Actual:   7 minutes
"""
from prac_06.guitar import Guitar
Gibson_L_5_CES = Guitar("Gibson_L_5_CES",1922,16035.04)
Another_Guitar = Guitar("Another_Guitar",2013,10000)
print(Gibson_L_5_CES)
print(Gibson_L_5_CES.get_age())
print(Another_Guitar)
print(Another_Guitar.is_vintage())
print(Another_Guitar.get_age())
print(Gibson_L_5_CES.is_vintage())