"""
Write a Python script to sort (ascending and descending) a dictionary by
value. 
"""

di={1:2,3:4,4:3,2:1,0:0}
print("Dic : ",di)

li=list(di.items())
print("List : ",li)

li.sort()
print('Ascending order is :',li)

li.reverse()
print('Descending order is :',li)