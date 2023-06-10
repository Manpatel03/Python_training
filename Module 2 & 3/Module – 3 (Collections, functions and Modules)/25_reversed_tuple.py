"""
Write a Python program to reverse a tuple.
"""

tup1 = (0,1,2,3,4)

rev = reversed(tup1) #reversed method use to reverse tuple element

print(tuple(rev)) #print reversed tuple


# Reversing a tuple using slicing
# New tuple is created
def Reverse(tuples):
	new_tup = tuples[::-1]
	return new_tup
	
# Driver Code
tuples = ('0','1','2','3')
print(Reverse(tuples))
