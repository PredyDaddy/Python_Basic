import random
z = list()
def generateAnswer():
    x = random.randrange(1,99)
    return(x)

def checkPrevious(a):
    if a not in z:
        return True
    return False

def analyseGuess(x): 
    times = 0
    while(times < 10):
        
        a = int(input("Please Guess:"))
        if checkPrevious(a):
            z.append(a)
            times += 1
            if  a == -1:
                break
            elif a == x:
                print('The game is won') 
                break
            elif a > x:
                print('Too high')
            elif a < x:
                print('Too low')
        else:
            print('You tried it already')
               

x = generateAnswer()
analyseGuess(x)



