# Using two loops, create a bubble sorter that can sort a Python list. You sorter 
# should ignore case in performing the sort. 
x=['gnu', 'aardvark', 'horse', 'donkey', 'eagle', 'emu']
a=len(x)
for i in range(a-1):
    for j in range(i,a-1):
        if x[i] > x[i+1]:
            x[i+1],x[i] = x[i],x[i+1]
        
        
print(x)
            
    

