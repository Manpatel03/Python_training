"""Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings."""

li = ['abw', 'aba','122','ama','mam']
x = 0
for i in li:
    if len(li) > 2 and i[0] == i[-1]:

        x=x+1
        temp = i
    
print("count the number of string is :",len(li))
print("first and last character are same is :",temp,x)

