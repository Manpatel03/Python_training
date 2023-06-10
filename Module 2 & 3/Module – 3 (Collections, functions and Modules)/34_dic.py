"""34.Write a Python script to check if a given key already exists in a
dictionary.
"""

dict = {1:30,2:40,3:10,4:50}

key = int(input("Enter key to check in dictionary : "))

if  key in dict:
    print("key already exist in dictionary")
else:
    print("key is not present in dictionary")
        
