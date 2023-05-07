"""Write a Python function that takes a list and returns a new list with unique
elements of the first list. """

ul=[1,2,4,5,6,5]
nl = []
for i in ul:
    if i not in nl:
        nl.append(i)

        
    
        
print(nl)