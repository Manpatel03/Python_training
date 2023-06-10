"""
Write a Python program to replace last value of tuples in a list.
"""

l1 = [(21),(42),(13),(12),(98),(3),(12)]

l1[-1] = 1203

print(l1)



l = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (3,) for t in l])