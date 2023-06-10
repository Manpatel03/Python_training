"""Write a Python program to check whether a list contains a sub list """

list1 = [1,3,8,12,13,18,21]
list2=[1,3,12,18]

for i in list1:
    for j in list2:
        if i==j:
            print(i)