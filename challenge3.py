# #Create a list comprehension and use it to display only the even numbers 
# in a given list. 
Given =[1,2,3,4,5,6,7,8,9,10]
Even = [i for i in Given if i%2 ==0]
print(Given,Even)


# Create a list comprehension that produces a new list b from a given list of 
# strings a consisting of only those elements in a that have 3 or fewer 
# characters. 
a = ['leaning Python','只因','is such','你','a painstaking','太','process','TAT.','美',]
b= [i for i in a if len(i)<=3]
b

# Create a list comprehension that produces a new list b from a given list of 
# strings a consisting of only those elements in a that begin with a specific 
# letter. 
a = ['leaning Python','只因','is such','你','a painstaking','太','process','TAT.','美',]
b= [i for i in a if i.find('p')>=0]
b


# Create a list comprehension that produces a new list b from a given list of 
# strings a consisting of only those elements in a that begin with a specific 
# letter and have 3 of fewer characters. 
a = ['leaning Python','只因','is such','你','a painstaking','太','process','TAT.','美','p']
b= [i for i in a if i.find('p')>=0 and len(i)<=3]
b
