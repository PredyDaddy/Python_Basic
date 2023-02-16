# ● Create a random number generator function that takes two parameters e.g. genRandom(minVal, maxVal) ,,
# and then returns an output value between those two values inclusive.
import random
minVal = int(input('Please enter the minVal:'))
maxVal = int(input('Please enter the maxVal:'))
def genRandom(minVal, maxVal):
    
    return random.randrange(minVal,maxVal)

print(genRandom(minVal, maxVal))


# ● Create a function to generate a lottery ticket. A lottery ticket can be conveniently represented using a list of 6 integer numbers with values between  . 
# The function should return the list. 
# Numeric values in a list can be sorted into ascending order using list.sort(reverse=??) where list is the list you want sorted a keyword argument reverse is used (value True or False) to specify whether you want ascending or descending order. 
# There should be no duplicate values in your list.

import random
def ReturnList():
    i = random.randrange(1,10)
    a = list()
    temp = list()
    while (len(temp)<6):
        a.append(i)
        temp = list(set(a))
        i = random.randrange(1,10)
    temp.sort(reverse = False)   #Function sort return None
    return temp






# ● Create a function to check whether we have won the lottery. 
# This function should take the lottery ticket list previously created as one parameter, and a list of the 6 winning numbers as the other argument. 
# If 2 numbers match return a win of £1. If 3 numbers match, the function should return a win of £10, if 4 numbers match, return a win of £50, 5 number a win of £500 and 6 numbers £1,000,000.

import random
WinNumber = list(1,4,5,6,7,8)
def ReturnList():
    i = random.randrange(1,10)
    a = list()
    temp = list()
    while (len(temp)<6):
        a.append(i)
        temp = list(set(a))
        i = random.randrange(1,10)
    temp.sort(reverse = False)   #Function sort return None
    return temp

set_c = set(WinNumber) & set(ReturnList())
if len(set_c) == 2:
    print('You win £1')
elif len(set_c) == 3:
    print('You win £10')
elif len(set_c) == 4:
    print('You win £50')
elif len(set_c) == 5:
    print('You win £500')
elif len(set_c) == 6:
    print('You win £1000')
else:
    print('You win nothing')