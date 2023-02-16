# Allow the user to enter a number. Use an if statement to display whether 
#the number is negative, equal to zero or positive.
i = int(input('Please input a number')) 
if i == 0:
    print('The number is equal to zero')
if i >0:
    print('Positive')
else:
    print('Negative')

# Allow the user to enter a number and then 
#iterate over the range to determine whether the number the user entered 
#is present in the sequence. 
a = int(input('Please input a number'))
if a in range(0,99):
    print('%d is in the sequence' %a)

# Allow the user to enter values for the initial value and common 
#difference. Write code to determine the sum of the first 10 elements in the 
#arithmetic sequence. 
b = int(input('Please input the initial number'))
c = int(input('Please input the common difference'))
sum = 0
for x in range(b,b+c*10,c):
    sum=sum+x
    print(sum)

# Write code to simulate the simple children’s game “Fuzz Buzz”
for i in range(1,51):
    if i%5 == 0:
        print('Fuzz')
    elif i%6 == 0:
        print('Buzz')
        if i%5 ==0 and i%6 ==0:
            print('Fuzz Buzz')
    else:
        print(i)