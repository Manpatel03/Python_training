"""
Write a Python program to convert a tuple to a string. 
"""

tup1 = ("m","a","n")
print(tup1)
st = ''.join(tup1)

print(st)

print(type(st)) #check the convert tuple to string


"""
Write a Python program to convert a tuple to a string using for loop
"""
# Defining a Python tuple
tp = ('Man ', 'Patel ')

# Creating an empty Python string
st = ''

# Using the Python for loop to convert the tuple to a string
for i in tp:
    st = st + i

# Printing the results
print("Given Python tuple: ", tp)
print("Generated Python string: ", st)

# Validating the type of 'st'
print(type(st))