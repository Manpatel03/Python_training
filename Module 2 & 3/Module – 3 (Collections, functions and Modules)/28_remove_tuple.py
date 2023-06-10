""""Write a Python program to remove an empty tuple(s) from a list of tuples."""
list = [(1,2,3),(4,5),()]

for tuple in list:
    print(tuple)
    if (len(tuple)==0):
        list.remove(tuple)
        
print(list)
