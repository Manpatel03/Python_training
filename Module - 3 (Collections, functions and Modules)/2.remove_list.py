"""How will you remove last object from a list? 
Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?"""

list1 = [2,33,222,14,25]
i=0
l1=len(list1)
#print(l1)
for i  in range (4):
    if i > list1:
        list1.remove(-1)
    print(list1)