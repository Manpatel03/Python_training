# 02) Write a Python program to get the Factorial number of given number.

num = int(input("Enter a number : "))
fac =1
i=1
while i<=num: #check condition 1 2 3 4 5
    fac =fac*i # 1 2 6 24 120
    i=i+1
print("The factorial of",num,"is",fac)