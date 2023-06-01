"""Write a Python program to print all unique values in a dictionary"""
d={"1":"abc"}, {"2": "def"}, {"3": "ghi"}, {"4": "jkl"}, {"5":"mno"}, {"5":"pqr"},{"6":"stu"}
a=[]
for i in d:
    for j in i.values():
        a.append(j)
print(set(a))