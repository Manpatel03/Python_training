"""
Write a Python script to sort (ascending and descending) a dictionary by
value. 

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items())

print('Dictionary in ascending order by value : ',sorted_d)

sorted_l = d.sort(reverse = True)

print('Dictionary in descending order by value : ',sorted_l)
"""
d={1:2,3:4,4:3,2:1,0:0}
l=list(d.items())
l.sort()
print('Ascending order is',l)
l=list(d.items())
l.sort(reverse=True)
print('Descending order is',l)