"""Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. 
Sample string: 'w3resource' 
Expected output: 
{'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}"""

str = 'w3resource'
dict1 = {}
count1 = 0
for i in str:
   count1= str.count(i)
   dict1[i]=count1
print("String : ",str)
print("count of the letters from string : ",dict1)