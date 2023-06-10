"""Write a Python program to combine two dictionary adding values for 
common keys."""

dict1 = {'a': 300, 'b': 400, 'c':600}  
dict2 = {'a': 500, 'b': 300, 'c':300}  
dict3= {}  

dict3.update(dict1,)
dict3.update(dict2)

for i,j in dict1.items():  # a: 300,b:400 ,c:600
    for x,y in dict2.items(): # a : 500,b:300,c:300
        if i ==x:  
            dict3[i] = j+y # a : 800 ,b:700 ,c:900
print(dict3)