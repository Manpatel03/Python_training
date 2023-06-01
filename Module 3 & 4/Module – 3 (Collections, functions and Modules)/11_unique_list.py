"""Write a Python function that takes a list and returns a new list with unique
elements of the first list. """

ul=[1,2,3,4,5,6,3]
nl = []
for i in ul:
    if i not in nl:
        nl.append(i)   
print(nl)