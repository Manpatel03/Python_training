"""
20) Write a Python function that takes a list of words and returns the length
of the longest one.

"""
# function to find the longest
# length in the list
def longestLength(n):
	max = len(n[0])
	temp = n[0]

	# for loop to traverse the list
	for i in n:
		if(len(i) > max):

			max = len(i)
			temp = i
			
	print("The word with the longest length is:", temp,
		" and length is ", max)

# Driver Program
n = ["man", "patel", "python", "programming"]
longestLength(n)
