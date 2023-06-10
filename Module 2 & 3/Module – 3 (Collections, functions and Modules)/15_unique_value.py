"""Write a Python program to get unique values from a list"""
ul=[1,2,3,3,4,4,5]
nl = []
for i in ul:
    if i not in nl:
        nl.append(i) 
print(nl)