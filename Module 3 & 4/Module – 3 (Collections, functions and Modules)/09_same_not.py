"""Write a Python function that takes two lists and returns true if they have
at least one common member."""

list1 = [10,20,30,40,50]
list2 = [30,20,60,70,80,90,100]

result = False
for i in list1:
    for j in list2:
        if i==j:
            result = True
print(result)
    