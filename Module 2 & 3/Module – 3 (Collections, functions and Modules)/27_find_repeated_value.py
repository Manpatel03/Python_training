"""
27) Write a Python program to find the repeated items of a tuple.
"""

l1 = [(1,2), (2,3), (3,4), (4,5)]
d = dict(l1)
print(d)



tup=(1,3,4,32)  
for i in tup:
    if i == tup:
        print('repeated')
    else :
        print('not repeated')


# not complate

