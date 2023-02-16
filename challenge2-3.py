# Allow the user to enter an int number. Determine if the
# number is prime or not. A number is prime if it is only
# divisible exactly by 1 and itself, e.g. 3, 7, 11 and 17.
# 2 is the only even prime number. 1 is not generally regarded
# as prime. Display the answer “prime” or not prime as appropriate.
x = int(input('Enter the number to test: '))
isPrime = True # boolean data type - note capital T
if x <= 1:
    isPrime = False
else:
     for i in range(2,x//2+1):
        if x % i == 0:
           isPrime = False
           break

print(isPrime)
