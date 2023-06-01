"""Write a Python program to remove duplicates from a list."""

li = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40,40,40,221]
print(li)
# print(li.count(40))

for i in li:
    if li.count(i) > 1:
        li.remove(i)
        
print(li) 
    
