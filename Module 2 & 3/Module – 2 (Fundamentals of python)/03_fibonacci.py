# Write a Python program to get the Fibonacci series of given range.

num = int(input("Enter Number :"))

x,y,z = 0,1,0

while z<=num:
     print(z)# 0 1 1 2 3 5 8 
     x= y # 1 0 1 1 2
     y=z # 0 1 1 2 3
     z=x+y# 1 1 2 3 5