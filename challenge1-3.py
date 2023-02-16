# Generate a sequence of int numbers in the pattern 0, 2, 4 …. up
# to 20 inclusive and display the numbers on the screen.

x = 0
while x<= 20:
    if  x%2 == 0:
        print(x)    
    x += 1


# Allow the user to enter a string, and then print out each letter
# in the string one at a time on a separate line.

a = input('Enter some text: ')
for each in a:
    print(each)

# As above, but print out the letters in the string in reverse order.

a = input('Enter some text: ')
for each in a[::-1]:
    print(each)
    

# Starting with the initial value 0 and 1, generate a Fibonacci sequence.
# Each element in a Fibonacci sequence is the sum of the two previous
# elements e.g. 0, 1, 1, 2, 3, 5, 8 ……
# Allow the user to specify how many elements should be generated.

x = int(input('How many elements? '))
def fibonacci1(n):
    a, b = 0, 1
    for i in range(n):
        c = a
        a = b
        b = c + b
        
        print(b, end="\t")
 
fibonacci1(x)


